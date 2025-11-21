[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7TPcE591)
# Project 2: Reproducibility in Natural Language Processing


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/proj02-group10.git/HEAD)


Team Members 
Larissa Arreola, Vittal Vasudevan, Daniel Porter, Emily Ma


## Overview 
This project explores the reproducibility of the natural language processing (NLP) by doing analysis on the State of the Union speech dataset. 

The work in this repository includes 
- Data loading and exploratory data analysis (Part 1) 
- Text Processing with SpaCy (Part 2) 
- TF-IDF Vectorization and dimensionality reduction (Part 2) 
- Topic modeling with LDA and BERTopic (Part 3) 
- Additional analysis on word frequency over time (Part 4)

All work is done in a reproducible Jupyter Notebook environment, as noted with the ‘enviroment.yml’

click on the binder badge. Binder will launch Jupyterlab and load all dependencies automatically. 

Alternatively, One can run this repo locally by 

1. Create the environment 
```bash
   conda env create -f environment.yml
```

2. Activate the conda environment 
```bash
 conda activate proj02
```

Launch it


## Repository Structure 

The repository is structured as follows:

- `data/`  
  Contains the raw dataset used for analysis.  
  - `SOTU.csv` — State of the Union speech dataset

- `outputs/`  
  Contains all generated outputs from the notebooks, including saved figures.

- `src/`  
  Contains helper scripts and utility functions used throughout the project.  
  - `utils.py`

- `nlp-P01.ipynb`  
  Notebook for Part 1 — data loading and exploratory data analysis.

- `nlp-P02.ipynb`  
  Notebook for Part 2 — text processing with SpaCy and TF-IDF vectorization.

- `nlp-P03.ipynb`  
  Notebook for Part 3 — topic modeling using LDA and BERTopic.

- `nlp-P04.ipynb`  
  Notebook for Part 4 — word frequency analysis over time.

- `environment.yml`  
  The environment configuration file used to reproduce the computing environment (required for Binder).

- `myst.yml`  
  MyST metadata configuration file.

- `README.md`  
  Project overview, instructions for running the notebook, and reproducibility information.



## Reproducibility notes 
- All plots generated in Part 1,2,3,4 are saved automatically into the outputs folder, for interactive plots, a static image of them was saved.
- The project is fully reproducible by running the note book top-to-bottom.
- The environment is fully specified in the environment.yml for installation 
- Data files required for the analysis are included in the Data folder 
