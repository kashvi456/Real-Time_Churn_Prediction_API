from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

app = FastAPI(
    title="Real-Time Churn Prediction API",
    description="An API that predicts customer churn risk is real-time.",
    version="1.0.0"
)

model = joblib.load('models/decision_tree.pkl')

class CustomerData(BaseModel):
    tenure_months: int
    monthly_charges: float
    total_support_tickets: int
    days_since_last_login: int

@app.post("/predict_churn")
def predict_churn(customer: CustomerData):

    input_data = pd.DataFrame([{
        'tenure_months': customer.tenure_months,
        'monthly_charges': customer.monthly_charges,
        'total_support_tickets': customer.total_support_tickets,
        'days_since_last_login': customer.days_since_last_login
    }])

    prediction = int(model.predict(input_data)[0])

    probability = float(model.predict_proba(input_data)[0][1])

    if prediction == 1:
        action = "High Risk: Trigger 20% retention discount pop-up."
    else:
        action = "Low Risk: No action needed."

    return {
        "churn_prediction": prediction,
        "churn_probability": round(probability, 2),
        "recommended_action": action
    }