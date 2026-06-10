# 🚀 Real-Time Customer Churn Prediction API

A complete backend and Machine Learning pipeline that predicts if a customer is likely to cancel their subscription, allowing the business to automatically offer them a retention discount.

## 📌 Project Overview
Losing customers (churn) is a major problem for online businesses. Instead of waiting until the end of the month to see who canceled, this project evaluates a customer's live usage data to predict if they are unhappy *right now*.

When a user's data is sent to this API, it instantly calculates their risk level. If they are highly likely to cancel, the API returns a recommendation to trigger a 20% discount pop-up to save the customer.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Database:** MySQL, SQLAlchemy
* **Machine Learning:** Scikit-Learn (Decision Tree), Pandas
* **API Framework:** FastAPI, Uvicorn

## 🚀 How to Run the Project Locally
### 1. Database Setup
Run the database/schema.sql file in your MySQL environment to create the required tables.

### 2. Generate Data & Train the Model
(Note: Update the database connection string in the code with your MySQL password before running).

python scripts/generate_churn_data.py
python src/train_model.py
### 3. Start the API Server

uvicorn app:app --reload

## ⚡ Testing the API
* Once the server is running, FastAPI provides an interactive webpage to test the model.

* Open your browser and go to: http://127.0.0.1:8000/docs

* Expand the POST /predict_churn box and click "Try it out".

* Send a test JSON payload like this:

JSON
{
  "tenure_months": 2,
  "monthly_charges": 95.50,
  "total_support_tickets": 8,
  "days_since_last_login": 30
}
* Click Execute to see the AI instantly return a churn prediction and a recommended business action.

## 🧠 Why a Decision Tree?
A Decision Tree was chosen because it provides clear, easy-to-understand rules. Instead of the AI making decisions in secret, a Decision Tree works like a game of "20 Questions."
If a customer is flagged as high-risk, the business can trace the exact logic and see exactly why (e.g., "They had 8 support tickets and haven't logged in for 30 days"). This makes the model highly trustworthy and useful for business teams.
