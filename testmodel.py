# Testing the model just to make sure it works:

import joblib

# Loading model and vectorizer
model = joblib.load("classifier.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Defining category based on the source (incidents.csv)

category_mapping = {
    0: "Network Issue",
    1: "Server Issue",
    2: "Application Issue",
    3: "Security Issue",
    4: "Testing Issue"
}

# Testing the model
test_data = "[Computer is down and users cannot access services]"
transformed_data = vectorizer.transform([test_data])


#Getting the prediction label (number)
prediction = model.predict(transformed_data)[0]

# Converting numberic output to category
prediction = category_mapping[prediction]

print(f"Prediction: {prediction}")