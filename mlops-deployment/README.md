# How to Start

## Anaconda
If you are using anaconda for your local development.

**Requirements**
- Install Anaconda
- Open Anaconda and install jupyter notebook

Create a new ennvironment from base.
```bash
conda create -n mlopsv2 anaconda
```

Activate the new created environment
```bash
conda activate mlopsv2
```

Install the craeted environment to select from ipykernel
```bash
python -m ipykernel install --user --name=mlops-v2-env --display-name "Python (mlopsv2-env)"
```

