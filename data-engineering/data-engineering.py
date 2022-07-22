import argparse,json,os
    
# retrieve output location
parser = argparse.ArgumentParser()
parser.add_argument('--training_folder', type=str, dest='training_folder')
args, unknown_args = parser.parse_known_args()
training_folder = args.training_folder
print("training_folder:", training_folder)

# simulating reading tenants from DB
tenants = []
for i in range(1, 100):
    tenants.append({ "id": str(i) })

# dump tenant metadata/data into one file per tenant for further processing by parallel run step
for tenant in tenants:
    tenant_metadata_file_name = "tenant_" + tenant['id'] + '.json'
    with open(os.path.join(training_folder,tenant_metadata_file_name),'w') as tenant_metadata_file:
        json.dump(tenant,tenant_metadata_file)