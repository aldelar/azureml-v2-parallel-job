import argparse,os
import pandas as pd
import mltable

# evaluation
def evaluation(args):
    # open up the predictions file
    predictions_df = mltable.load(args.predictions_data_file).to_pandas_dataframe()
    print(f"predictions_df: {predictions_df}")
    
# read arguments
def parse_args():
    # retrieve output location
    parser = argparse.ArgumentParser()
    parser.add_argument('--predictions_data_file', type=str)
    args, unknown_args = parser.parse_known_args()
    print(f"predictions_data_file: {args.predictions_data_file}")
    return args

# main
if __name__ == "__main__":
    args = parse_args()
    evaluation(args)