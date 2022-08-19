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

### Data analysis:

- [EDA of IPC data](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/IPC_EDA.ipynb)
- [EDA of World Bank data](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/world_bank_EDA.ipynb)
- [EDA of FSNAU data](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/fsnau_EDA.ipynb)
- [Survival analysis and analysis into model performance](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/survival_analysis.ipynb)

### Twitter analysis:

- [Obtaining tweets](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/obtaining_twitter_data.ipynb)
- [Author analysis (anonimized)](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/twitter_exploration.ipynb)
- [Geotag estimation](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/twitter_data_geotags.ipynb)
- [Labeling tweets using NLP](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/labeling_tweets.ipynb)
- [Regression analysis](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/twitter_data_regressions.ipynb)
- [Regression analysis (Kenya)](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/twitter_data_kenya_regressions.ipynb)

### Gaurdian anlysis:

- [Obtaining the articles (script file)]()
- [Sentiment labeling](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/guardian_sentiment_labeling.ipynb)
- [Sentiment analysis](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/guardian_analysis.ipynb)

### Predictive modeling:

- [Model fitting, evaluation and hyperparameter tuning](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/twitter_data_geotags.ipynb)

- [Replication in ethiopia](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/twitter_data_geotags.ipynb)

### Satellite images:

- [Obtaining the images](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/sentinel_processing.ipynb)
- [Encoding the images](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/encoding_satellite_images.ipynb)
- [Predicting weather indices from encodings](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/autoencoder_ndvi.ipynb)
- [(Failing to) predict IPC phase from encodings](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/autoencoder_ipc.ipynb)
- [Soil moisture](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/soil_moisture_satellite.ipynb)
