import argparse,os,time
import pandas as pd

import tensorflow as tf

from azureml_user.parallel_run import EntryScript

# init() called once per process
def init():

    # retrieve parameters from the entry script
    parser = argparse.ArgumentParser()
    parser.add_argument("--param_1", type=str)
    parser.add_argument("--predictions_data_folder", type=str)
    args, unknown = parser.parse_known_args()
    global param_1
    global predictions_data_folder
    param_1 = args.param_1
    predictions_data_folder = args.predictions_data_folder

    # retrieve environment variables
    global env_var_1
    env_var_1 = os.environ['env_var_1']

    # AML logger
    global logger
    logger = EntryScript().logger
    logger.info(f"train init(), param_1:{param_1}, env_var_1:{env_var_1}")
   
# run() called as many times as needed to process all files in the parallel job input
def run(mini_batch):
    
    results = []
    logger.info(f"train run({mini_batch})")
    for tenant_file_path in mini_batch:
        tenant_basename = os.path.basename(tenant_file_path)
        # process the tenant training data file to train a model + infer predictions for the final evaluation step
        with open(tenant_file_path,'r') as tenant_file:
            tenant_df = pd.read_csv(tenant_file)
        logger.info(f"train processing({tenant_basename} => {tenant_df}) with param_1:{param_1}, env_var_1:{env_var_1}")
        # TODO: replace this part with your model training
        logger.info("training model...")
        time.sleep(5) 
        # TODO: write the output of your models predictions for further performance evaluation of your strategy
        with open(os.path.join(predictions_data_folder,tenant_basename),'w') as prediction_file:
            tenant_df.to_csv(prediction_file,index=False)
        # log to global results object
        results.append(f"{tenant_basename} processed")

    return results

# main() called once per process
if __name__ == '__main__':
    #
    init()
    # retrieve the input data from the entry script
    input_data_files = ['/datalake/json_folder/file1.json', '/datalake/json_folder/file2.json', '/datalake/json_folder/file3.json']
    results = run(input_data_files)
    # log the results
    logger.info(f"train results:{results}")