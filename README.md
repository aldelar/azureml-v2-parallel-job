# azureml-v2-parallel-training

## project description

This is an Azure ML CLIv2 template project demonstrating the use of the parallel job type.

We here have a simple pipeline with 2 steps:
- data-engineering, which would grab data from a data source and generate training data sets (assuming we'd be training one model per dataset in the next step, multi-model scenario)
- training: setup to run on a compute cluster (multi nodes + multiple training processes per node) which dispatches each training data set to the processes in the cluster to get through the workload

This template showcases how to pass training jobs parameters either as:
- environment variables which will automatically be setup on all training nodes (see 'env_var_1' in pipeline.yml and training.py)
- training script parameters (see 'param_1' in pipeline.yml and training.py)

## how to create and run the pipeline

[Install the Azure CLI + the Azure CLI 'ml' extension](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-cli?tabs=public), then run:

```
AZURE_ML_CLI_PRIVATE_FEATURES_ENABLED=true az ml job create -f pipeline.yml --web
```