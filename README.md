# Introduction
This repository is a template ML pipeline that can be used to do any deep learning calculation.
THIS IS STILL A WORKING PROCESS. Here is the broad roadmap:
1. Make run template
2. Make input processor
3. Make model processor
4. Make training processor
5. Make output processor
6. Make analysis

# Installation
Ensure the correct dependencies are installed. This repo is build with conda in mind.
```bash
conda env create -f environment.yml
```

# Usage
Make sure the program is run in the correct environment
```bash
conda activate ann
```
there are several file that can be run:
1. run.py consists of full automatic run
2. cli.py to run the program interactively
3. analysis.ipynb consists of typical analysis that can be done
