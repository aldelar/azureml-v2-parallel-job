FROM mcr.microsoft.com/azureml/openmpi4.1.0-cuda11.2-cudnn8-ubuntu20.04:20220902.v1

ENV AZUREML_CONDA_ENVIRONMENT_PATH /azureml-envs/tensorflow-2.7
# Create conda environment
RUN conda create -p $AZUREML_CONDA_ENVIRONMENT_PATH \
    python=3.8 pip=20.2.4

# Prepend path to AzureML conda environment
ENV PATH $AZUREML_CONDA_ENVIRONMENT_PATH/bin:$PATH

# Install pip dependencies
RUN HOROVOD_WITH_TENSORFLOW=1 pip install 'matplotlib~=3.5.0' \
                                          'psutil~=5.8.0' \
                                          'tqdm~=4.62.0' \
                                          'pandas~=1.3.0' \
                                          'scipy~=1.7.0' \
                                          'numpy~=1.21.0' \
                                          'ipykernel~=6.0' \
                                          'azureml-core==1.45.0' \
                                          'azureml-defaults==1.45.0' \
                                          'azureml-mlflow==1.45.0' \
                                          'azureml-telemetry==1.45.0' \
                                          'tensorboard~=2.7.0' \
                                          'tensorflow-gpu~=2.7.0' \
                                          'tensorflow-datasets~=4.5.0' \
                                          'onnxruntime-gpu~=1.9.0' \
                                          'protobuf~=3.20' \
                                          'horovod[tensorflow-gpu]~=0.23.0'
                          
# This is needed for mpi to locate libpython
ENV LD_LIBRARY_PATH $AZUREML_CONDA_ENVIRONMENT_PATH/lib:$LD_LIBRARY_PATH