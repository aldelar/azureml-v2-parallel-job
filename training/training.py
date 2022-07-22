import argparse,json,os,time

# init() called once per process
def init():

    parser = argparse.ArgumentParser()
    parser.add_argument("--param_1", type=str)
    args, unknown = parser.parse_known_args()
    global param_1
    param_1 = args.param_1

    print("train init()")
    print(f"train init(), param_1:{param_1}")
   
# run() called as many times as needed to process all files in the parallel job input
def run(mini_batch):
    
    results = []
    print(f"train run({mini_batch})")
    for tenant_file_path in mini_batch:
        tenant_basename = os.path.basename(tenant_file_path)
        with open(tenant_file_path,'r') as tenant_file:
            tenant_dict = json.load(tenant_file)
        print(f"train processing({tenant_basename} => {tenant_dict}) with param_1:{param_1}")
        time.sleep(0.5) # simulate some small processing

        results.append(f"{tenant_basename} processed")

    return results