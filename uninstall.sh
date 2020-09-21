#!/bin/bash

#removing link
sudo rm -rf /usr/local/bin/ctr
#removing conda env and dependencies. Also clone folder
#NOTE: removes clone folder also.
eval "$(conda shell.bash hook)"
conda deactivate
conda remove --name ctr-env --all
rm -rf ../Colab-Connect






