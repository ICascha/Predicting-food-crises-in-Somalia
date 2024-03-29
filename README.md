# Predicting food crises in Somalia

Master thesis project

**IMPORTANT DISCLAIMER**: This repositry is meant for replication of my master's thesis. Most results in during the thesis turned out negative, most importantly using **Satellite images**. I do not recommend to take this approach in future research as it requires a large amount of computational resources and time. I have tested many setups around this approach and they all failed to deliver results.

If you run into any issues/have any questions let me know on my [email](mailto:caschavanwanrooij@gmail.com) or open
an issue on this GitHub repo. **Feel free to mail for anything related to this project or a continuation!**.

The easiest way to set up an environment for this project is to use a [Anaconda](https://www.anaconda.com/) virtual environment. Open up an anaconda prompt and run the following commands:

```
conda create -n msc_thesis_food_insecurity
conda activate msc_thesis_food_insecurity
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict
conda install python=3 geopandas
conda install -c conda-forge linearmodels
```

Alternatively, this project can be opened in Google Colab where most required dependencies are installed by default:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ICascha/Predicting-food-crises-in-Somalia)

If you get an error that a package is missing (for example, geopandas or linearmodels), then you can install these packages by opening a new code cell and running the following code:

```
!pip install PACKAGE_NAME
```

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

- [Obtaining the articles (script file)](https://github.com/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/auxiliary_code/gaurdian_download.py)
- [Sentiment labeling](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/guardian_sentiment_labeling.ipynb)
- [Sentiment analysis](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/guardian_analysis.ipynb)

### Predictive modeling:

- [Model fitting, evaluation and hyperparameter tuning](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/model_fitting.ipynb)
- [Replication in ethiopia](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/ethiopia_replication.ipynb)

### Satellite images:

- [Obtaining the images](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/sentinel_processing.ipynb)
- [Encoding the images](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/encoding_satellite_images.ipynb)
- [Predicting weather indices from encodings](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/autoencoder_ndvi.ipynb)
- [(Failing to) predict IPC phase from encodings](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/autoencoder_ipc.ipynb)
- [Soil moisture](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/soil_moisture_satellite.ipynb)

## Prerequisites for replication:

### Credentials

Obtain login credentials for:

- [FSNAU database](https://fsnau.org/ids/)
- [Twitter v2 API Academic Research access](https://developer.twitter.com/en/products/twitter-api/academic-research)
- [Guardian API](https://open-platform.theguardian.com/)

Fill in the requested credentials them in in the following [file](https://github.com/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/auxiliary_code/login_data.py)

For the sattelite images in the notebook you will need to obtain a client ID and client secret. First create an [account](https://www.sentinel-hub.com/), then follow this [guide](https://sentinelhub-py.readthedocs.io/en/latest/configure.html).

- Fill the credentials in in the first codeblock of [this notebook](https://nbviewer.org/github/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/sentinel_processing.ipynb)

### Order of execution

- Run [dataset_processing](https://github.com/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/auxiliary_code/dataset_processing.py)
- Run the [FSNAU scraper](https://github.com/ICascha/Predicting-food-crises-in-Somalia/blob/main/notebooks/auxiliary_code/fsnau_scraper.ipynb)
- Run all data anlysis notebooks
- Any of the other notebook categories described above can be run independently after these steps. Do make sure to run the notebooks in the order given above within a category.

### Colab specifics

For all notebooks that require neural network training it is advised to rune these on Colab with the GPU option, a guide is given [here](https://www.tutorialspoint.com/google_colab/google_colab_using_free_gpu.htm). You will also need to upload some files either to the Colab instance directly, this can be done in the menu at the left of the screen:

![Upload Colab Example](https://github.com/ICascha/Predicting-food-crises-in-Somalia/blob/main/upload_file_colab.png)

This works fine for small files, but for big files (like gaurdian.json), this is really slow. It is best to upload large files to your google drive. Then, you can link your google drive with the colab session using this [tutorial](https://www.marktechpost.com/2019/06/07/how-to-connect-google-colab-with-google-drive/). Your drive will be mounted at the location /content/drive/.

You can download the results of the Colab session while the session is still running like so:

![Download Colab Example](https://github.com/ICascha/Predicting-food-crises-in-Somalia/blob/main/download_file_colab.png)
