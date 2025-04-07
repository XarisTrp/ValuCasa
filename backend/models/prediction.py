import numpy as np
import pandas as pd
from models.model_loader import best_model

def make_prediction(df_processed: pd.DataFrame) -> float:
    prediction = best_model.predict(df_processed)
    return float(np.expm1(prediction)[0])
