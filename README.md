# azureml-v2-parallel-training

## project description

This is an Azure ML CLIv2 template project demonstrating the use of the parallel job type.

We here have a simple pipeline with 2 steps:
- data-engineering, which would grab data from a data source and generate training data sets (assuming we'd be training one model per dataset in the next step, multi-model scenario)
- training: setup to run on a compute cluster (multi nodes + multiple training processes per node) which dispatches each training data set to the processes in the cluster to get through the workload

This template showcases how to pass training jobs parameters either as:
- environment variables which will automatically be setup on all training nodes (see 'env_var_1' in pipeline.yml and training.py)
- training script parameters (see 'param_1' in pipeline.yml and training.py)

The input of a parallel job relies on an [MLTable](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-register-data-assets?tabs=CLI#create-a-mltable-data-asset) source.
Please have a look at the data-engineering.py code which generates an MLTable descriptor alonside the data (two ways defined there, explicit list of all files to be included as the MLTable definition, or use of * qualifier to grab everything in the folder). An MLTable can describe a Tabular data set (and apply transformations on the fly) or a File dataset (any type of file for a wide range of use cases).

The training job outputs fake predictions of the models to the 'prediction_data_folder' output, showcasing how to capture artifacts into a specific datalake location. The 'datalake' datastore has to be defined in your Azure ML environment, and would be pointint to a storage account container. The folder (path) defined in 'prediction_data_folder' will be created automatically in the datalake if it doesn't exist already.

```
outputs:
      prediction_data_folder:
        type: uri_folder
        path: azureml://datastores/datalake/paths/aml_v2_pj_prediction_data
        mode: rw_mount
```

## how to create and run the pipeline

[Install the Azure CLI + the Azure CLI 'ml' extension](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-cli?tabs=public), then run the following to create the steps runtime environment (repeat this any time you need to modify the 'conda' files in each step folder to support code changes):

```
az ml environment create -f ./data-engineering/data-engineering-environment.yml
az ml environment create -f ./training/training-environment.yml
```
To trigger a pipeline creation/run, run the following (note the flag to turn on the parallel job private preview feature if it isn't in public preview when you run this):

```
AZURE_ML_CLI_PRIVATE_FEATURES_ENABLED=true az ml job create -f pipeline.yml --web
```