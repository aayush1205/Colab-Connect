#!/bin/bash
#env ops
conda env create -f env.yaml
eval "$(conda shell.bash hook)"
conda activate ctr-env
pip install -r requirements.txt
code --install-extension ms-vscode-remote.remote-ssh
code --install-extension ms-python.python


SHELL_TARGDIR="/usr/local/bin"
REPO_TARGDIR="/usr/local"
CURRDIR=$(readlink -f "$0")
CURRDIR=$(dirname "$CURRDIR")
python $CURRDIR/src/add-binding.py
sudo ln -s $CURRDIR/ctr /usr/local/bin
chmod +x /usr/local/bin/ctr
chmod +x ./uninstall.sh

