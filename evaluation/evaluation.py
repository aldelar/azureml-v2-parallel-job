import argparse,os
import pandas as pd
import mltable

# evaluation
def evaluation(args):
    # open up the predictions file
    predictions_mlt = mltable.load(args.predictions_mltable)
    print(f"predictions_mlt: {predictions_mlt}")
    print(f"predictions_mlt.paths: {predictions_mlt.paths}")
    predictions_df = predictions_mlt.to_pandas_dataframe()
    print(f"predictions_df: {predictions_df}")
    
# read arguments
def parse_args():
    # retrieve output location
    parser = argparse.ArgumentParser()
    parser.add_argument('--predictions_mltable', type=str)
    args, unknown_args = parser.parse_known_args()
    print(f"predictions_mltable: {args.predictions_mltable}")
    return args

# main
if __name__ == "__main__":
    args = parse_args()
    evaluation(args)