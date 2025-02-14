# Data Processing before it is fed into the model. 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Loading provided dataset using pandas
df = pd.read_csv("incidents.csv")

# Converting category Label to numbers
df["label"] = df["category"].astype("category").cat.codes

# Splitting the dataset into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(
    df["description"], df["label"], test_size=0.2, random_state=42
)

# Converting Description into Vector numerical
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)  # Learn from training data
X_test_tfidf = vectorizer.transform(X_test)  # Transform test data using the same model

# Saving the vectorizer using joblib
joblib.dump(vectorizer, "vectorizer.pkl")
joblib.dump((X_train_tfidf, X_test_tfidf, y_train, y_test), "processed_data.pkl")

print("Data Processing Completed")

