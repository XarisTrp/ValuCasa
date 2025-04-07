from fastapi import FastAPI, HTTPException
import pandas as pd
from schemas.request import HouseFeatures
from preprocessing.preprocessing import pre_process
from models.prediction import make_prediction
from utils.logger import logger

app = FastAPI(
    title="House Price Prediction API",
    description="API for predicting house prices based on input features.",
    version="1.0.0"
)

@app.post("/predict")
async def predict_house_price(features: HouseFeatures):
    try:
        input_df = pd.DataFrame([features.model_dump()])
        processed_data = pre_process(input_df)
        predicted_price = make_prediction(processed_data)
        return {"predicted_price": predicted_price}
    except ValueError as ve:
        logger.warning(f"Validation error: {ve}")
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logger.error(f"Prediction error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the House Price Prediction API. Use /predict endpoint."}

