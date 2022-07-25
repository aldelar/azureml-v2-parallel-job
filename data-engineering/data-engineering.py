import argparse,json,os

# data engineering
def prepare_training_data(args):
    # simulating reading tenants from DB
    tenants = []
    for i in range(1, 101):
        tenants.append({ "id": str(i) })
    # generate MLTable metadata file
    with open(os.path.join(args.training_data_folder,'MLTable'),'w') as MLTable_metadata_file:
        MLTable_metadata_file.write("paths:\n")
        # dump tenant metadata/data into one file per tenant for further processing by parallel run step
        for tenant in tenants:
            tenant_metadata_file_name = "tenant_" + tenant['id'] + '.json'
            with open(os.path.join(args.training_data_folder,tenant_metadata_file_name),'w') as tenant_metadata_file:
                # 'tenant' could contain your training data set if running in a non parallel step is efficient for this process
                # or here just an id, assuming you may use this id in the training step to directly retrieve data from a database
                # for instance at training time by each process (data engineering maybe done as a SQL query from your store)
                # note: you could also consider a multi-steps approach for your data prep:
                # 1. query your datastore to figure out which tenants need to be processed, collect their ids, generate id files as job definitions
                # 2. run a parallel step to generate the tenant training data files (actual data retrieval and engineering done on datalake at that point)
                # 4. pipe output of 2 to 3. (paralell step to do training)
                json.dump(tenant,tenant_metadata_file)
            print(f"{tenant_metadata_file_name} generated.")
            # add file to MLTable metadata file
            MLTable_metadata_file.write(f"  - file: ./{tenant_metadata_file_name}\n")
    
    # alternate MLTable metadata file content
    # paths:
    #  - file: ./*.json

# read arguments
def parse_args():
    # retrieve output location
    parser = argparse.ArgumentParser()
    parser.add_argument('--training_data_folder', type=str, dest='training_data_folder')
    args, unknown_args = parser.parse_known_args()
    print(f"training_data_folder: {args.training_data_folder}")
    return args

# main
if __name__ == "__main__":
    args = parse_args()
    prepare_training_data(args)