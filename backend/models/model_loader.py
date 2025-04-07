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
