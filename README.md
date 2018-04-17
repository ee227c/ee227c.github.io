# EE227C course page

Environment setup for running code (assumes you have Anaconda installed, download the most recent version [here](https://www.anaconda.com/download)):

```
ENVNAME=ee227c
conda create -y -n $ENVNAME python=3.6
source activate $ENVNAME
conda install -y -c anaconda numpy scipy matplotlib jupyter 
conda install -y -c omnia autograd
pip install sklearn
```
