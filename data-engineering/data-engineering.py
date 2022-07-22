import argparse,json,os

# data engineering
def prepare_training_data(args):
    # simulating reading tenants from DB
    tenants = []
    for i in range(1, 101):
        tenants.append({ "id": str(i) })
    # dump tenant metadata/data into one file per tenant for further processing by parallel run step
    for tenant in tenants:
        tenant_metadata_file_name = "tenant_" + tenant['id'] + '.json'
        with open(os.path.join(args.training_data_folder,tenant_metadata_file_name),'w') as tenant_metadata_file:
            json.dump(tenant,tenant_metadata_file)
        print(f"{tenant_metadata_file_name} generated.")

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