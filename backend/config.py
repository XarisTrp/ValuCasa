import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATHS = {
    "model": os.path.join(BASE_DIR, "artifacts", "best_house_price_model_Random Forest.pkl"),
    "preprocessor": os.path.join(BASE_DIR, "artifacts", "house_price_preprocessor.pkl"),
    "geography_encoder": os.path.join(BASE_DIR, "artifacts", "geography_encoder.pkl"),
    "size_category_encoder": os.path.join(BASE_DIR, "artifacts", "size_category_encoder.pkl"),
}
