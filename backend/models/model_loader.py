import joblib
from utils.logger import logger
from config import MODEL_PATHS

def load_pickle(file_path):
    try:
        return joblib.load(file_path)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise RuntimeError(f"Missing required file: {file_path}")
    except Exception as e:
        logger.error(f"Error loading {file_path}: {e}")
        raise RuntimeError(f"Failed to load {file_path}: {e}")

best_model = load_pickle(MODEL_PATHS["model"])
preprocessor = load_pickle(MODEL_PATHS["preprocessor"])
geography_encoder = load_pickle(MODEL_PATHS["geography_encoder"])
size_category_encoder = load_pickle(MODEL_PATHS["size_category_encoder"])

logger.info("Models and preprocessors loaded successfully.")
