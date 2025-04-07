# MIT License
#
# Copyright (c) 2025 Spyros Mitsis
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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

