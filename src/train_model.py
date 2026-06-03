import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

from extract_data import get_training_data

def train_and_save_model():
    print("1. Fetching data from MySQL...")
    df = get_training_data()

    print("2. Preparing data for the Decision Tree...")

    X = df[['tenure_months', 'monthly_charges', 'total_support_tickets', 'days_since_last_login']]
    y = df['churned']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("3. Training the model...")
    clf = DecisionTreeClassifier(max_depth=4, random_state=42)
    clf.fit(X_train, y_train)

    print("4. Evaluating the model...\n")
    predictions = clf.predict(X_test)

    print("----Model Performance----")
    print(f"Accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%\n")
    print("Classification Report:\n", classification_report(y_test, predictions))

    os.makedirs('models', exist_ok=True)

    model_path = 'models/decision_tree.pkl'
    joblib.dump(clf, model_path)
    print(f"\nSuccess! Model saved to {model_path}")

if __name__ == "__main__":
    train_and_save_model()