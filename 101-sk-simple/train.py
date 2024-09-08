#!/usr/bin/env python3

import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load the dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Labels

# Step 2: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Choose a simple model (Decision Tree)
model = DecisionTreeClassifier()

# Step 4: Train the model
model.fit(X_train, y_train)

# Step 5: Save the trained model to a file
joblib.dump(model, 'trained_model.joblib')

# (Optional) Step 6: Load the model from the file
loaded_model = joblib.load('trained_model.joblib')

# Step 7: Make predictions with the loaded model
y_pred = loaded_model.predict(X_test)

# Step 8: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
