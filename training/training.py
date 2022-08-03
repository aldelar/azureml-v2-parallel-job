import argparse,json,os,time
from azureml_user.parallel_run import EntryScript

# init() called once per process
def init():

    # retrieve parameters from the entry script
    parser = argparse.ArgumentParser()
    parser.add_argument("--param_1", type=str)
    parser.add_argument("--prediction_data_folder", type=str)
    args, unknown = parser.parse_known_args()
    global param_1
    global prediction_data_folder
    param_1 = args.param_1
    prediction_data_folder = args.prediction_data_folder

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
        with open(tenant_file_path,'r') as tenant_file:
            tenant_dict = json.load(tenant_file)
        logger.info(f"train processing({tenant_basename} => {tenant_dict}) with param_1:{param_1}, env_var_1:{env_var_1}")
        time.sleep(2) # simulate some small processing
        # simulate write predictions to the output folder
        with open(os.path.join(prediction_data_folder,tenant_basename),'w') as prediction_file:
            json.dump(tenant_dict,prediction_file)
        # log to global results object
        results.append(f"{tenant_basename} processed")

    return results