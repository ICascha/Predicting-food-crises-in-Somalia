# Predicting food crises in Somalia

Master thesis project

The easiest way to set up an environment for this project is to use a [Anaconda](https://www.anaconda.com/) virtual environment. Open up an anaconda prompt and run the following commands:

```
conda create -n msc_thesis_food_insecurity
conda activate msc_thesis_food_insecurity
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict
conda install python=3 geopandas
```

Alternatively, this project can be opened in Google Colab where the required dependencies are installed automatically:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ICascha/Predicting-food-crises-in-Somalia)

## Notebooks:

- [Survival analysis and analysis into model performance](https://github.com/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/survival_analysis.ipynb)

### Twitter analysis:

- [Obtaining tweets](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/obtaining_twitter_data.ipynb)
- [Author analysis (anonimized)](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/twitter_exploration.ipynb)
- [Geotag estimation](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/twitter_data_geotags.ipynb)
- []
