## Readme

POC for ML training for IT Operations

## Objective

The goal of this project is to build a machine learning classifier that can categorise IT operations tickets based on historical incident data. 

The model will be trained on curated, tagged data and evaluated using [Scikit-Learn](https://scikit-learn.org/stable/) which is ML algorithm written in Python. 


## High Level Approach

1. Data Collection & Preprocessing (For this project we create dummy data (IT operations))
   *  For simplicity, created a incident file (incidents.csv), Description and Category
   *  Using Pandas to load the csv into a table, seems to be a popular choice for Data folks. It's also called Pandas Dataframe
   * `Machine learning models only understand numbers.` and I m converting `Category` field into numbers, this process is also called (Label Encoding). There is only 1 label field in a simple dataset like this. 
   Example below
```
description                     category              label

Server is down                  System Issue             1
Cannot connect to WiFi          Network Issue            0
Application keeps crashing      Application Issue        2
```
  * Next step is to split the dataset into training set (80%) and testing data (20%). This is to check if the model is accurate or not. [more here](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html). If we push all the data into the model, it will just memorise it, testing model is used to quiz the model. 
  * Next step is to comvert incident Description into a numerical format, and uses TF-IDF (Term Frequency-Inverse Document Frequency) to find important words. After conversion, it could be in a vector format `[0.2, 0.5, 0.1, 0.0, ...]` Common words like is, are get lower score wheras words like server, database gets higher score. [more here](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
  * 


## Things to consider

Evaluation Metrics: Precision, recall, F1-score, confusion matrix
Deployment: FastAPI, Flask, Docker (optional)
LLMs vs Traditional ML: If the dataset is large, LLMs can enhance contextual understanding.

## Contributors

* ALan
* Jonathan
* Suhail