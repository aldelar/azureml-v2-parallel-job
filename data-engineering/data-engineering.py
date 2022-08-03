import argparse,os
import pandas as pd

# data engineering
def prepare_training_data(args):
    # reading data from raw data file
    raw_data_df = pd.read_csv(args.raw_data_file)
    # TODO: data engineering here for what can be done accross all tenants in the source data...
    with open(os.path.join(args.training_data_folder,'MLTable'),'w') as MLTable_metadata_file:
        # start to generate MLTable metadata file
        MLTable_metadata_file.write("paths:\n")
        # We add a special file (task) to the descriptor
        # which will trigger the parallel step to generate the MLTable file for the predictions data set
        generate_mltable_for_predictions_filename = 'GENERATE-PREDICTIONS-MLTABLE'
        MLTable_metadata_file.write(f"  - file: ./{generate_mltable_for_predictions_filename}\n")
        # corresponding empty file saved into the ouput, will trigger the parallel step to generate the MLTable file for the predictions data set
        with open(os.path.join(args.training_data_folder,generate_mltable_for_predictions_filename),'w') as generate_mltable_for_predictions_file:
            generate_mltable_for_predictions_file.write("")
        # dump tenant metadata/data into one file per tenant for further processing by parallel run step
        for tenant_id in raw_data_df['tenant_id'].unique():
            # tenant specific data
            tenant_data_df = raw_data_df[raw_data_df['tenant_id'] == tenant_id]
            # TODO: potential extra data engineering at the tenant level
            # now save tenant training data to file into training data folder
            tenant_metadata_file_name = "tenant_" + str(tenant_id) + '.csv'
            with open(os.path.join(args.training_data_folder,tenant_metadata_file_name),'w') as tenant_metadata_file:
                tenant_data_df.to_csv(tenant_metadata_file,index=False)
            print(f"{tenant_metadata_file_name} generated.")
            # add file to MLTable metadata file descriptor
            MLTable_metadata_file.write(f"  - file: ./{tenant_metadata_file_name}\n")

    # alternate MLTable metadata file content (not safe if your destination folder isn't guaranteed to be empty when this runs)
    # paths:
    #  - file: ./*.json

# read arguments
def parse_args():
    # retrieve output location
    parser = argparse.ArgumentParser()
    parser.add_argument('--raw_data_file', type=str)
    parser.add_argument('--training_data_folder', type=str)
    args, unknown_args = parser.parse_known_args()
    print(f"raw_data_file: {args.raw_data_file}")
    print(f"training_data_folder: {args.training_data_folder}")
    return args

# main
if __name__ == "__main__":
    args = parse_args()
    prepare_training_data(args)