# SRF-UNet_OCTA

This project is a PyTorch implementation of using the SRF-UNet model for segmentation of OCTA images.

## Dependencies

This project requires the following packages:

- pytorch                   1.12.1          py3.9_cuda11.3_cudnn8_0
- tqdm
- numpy
- pandas
- albumentations
- opencv-python
- scipy
- matplotlib
- torchvision
- Pillow



Please ensure that you have installed the necessary software and environments before installing these dependencies.

## Usage

This project contains the following files and directories:

- `train.py`: A Python script used for model training.
- `results`: A directory containing the samples and metrics while training.
- `weights`: Model weights saved while training

Before using this project, please ensure that you have completed the following steps:

1. Downloaded or cloned this project.

2. Installed the necessary dependencies.

### Using train.py

train.py is the main script of this project, which implements the functionality of train stage. Before using this script, please ensure that you have installed Python and the necessary dependencies. The options are not given using argparse, but are listed at the beginning of train.py.

-- Epoches: the training epoches.
-- check_interval: save the weights and the test result while trained after xx epochs.
-- batch_size: the number of samples processed in training.
-- opt_step_size: the size of the update made to the model's parameters during the training process.
-- seg_lr: learing rate.
-- data_dir = data path of public dataset 'OCTA-500'.
-- other_info = some comments appended to the save files.

