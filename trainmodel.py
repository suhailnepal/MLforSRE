import joblib
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Loading the processed data
vectorizer = joblib.load("vectorizer.pkl")
X_train_tfidf, X_test_tfidf, y_train, y_test = joblib.load("processed_data.pkl")

# Training the model using Naive Bayes
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Evaluating the model
y_pred = model.predict(X_test_tfidf)
print(classification_report(y_test, y_pred))

# Saving the model
joblib.dump(model, "classifier.pkl")
print("Model Training Completed")

