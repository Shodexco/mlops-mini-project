from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
model = joblib.load("models/churn_model.joblib")

# Initialize FastAPI
app = FastAPI(title="Gym Churn Prediction API")

# Request body
class CustomerData(BaseModel):
    Near_Location: int
    Promo_friends: int
    Contract_period: int
    Month_to_end_contract: int
    Lifetime: int
    Avg_class_frequency_total: float
    Partner: int

# Home route
@app.get("/")
def read_root():
    return {"message": "Gym Churn Prediction API is running"}

# Prediction route
@app.post("/predict")
def predict_churn(data: CustomerData):
    input_data = np.array([[data.Near_Location,
                            data.Promo_friends,
                            data.Contract_period,
                            data.Month_to_end_contract,
                            data.Lifetime,
                            data.Avg_class_frequency_total,
                            data.Partner]])
    
    # Binary prediction
    prediction = model.predict(input_data)[0]
    # Probability prediction
    probability = model.predict_proba(input_data)[0][1]  # probability of churn = 1
    
    return {
        "Churn_Prediction": int(prediction),
        "Churn_Probability": round(float(probability), 4)
    }
