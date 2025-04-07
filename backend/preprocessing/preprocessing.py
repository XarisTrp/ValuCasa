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


import pandas as pd
from models.model_loader import preprocessor, geography_encoder, size_category_encoder
from preprocessing.feature_engineering import engineer_features

def pre_process(df: pd.DataFrame) -> pd.DataFrame:
    df = engineer_features(df)

    required_columns = ["geography", "size_category"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: '{col}'")

    df["geography"] = df["geography"].apply(lambda x: x if x in geography_encoder.classes_ else "Unknown")
    df["geography"] = geography_encoder.transform(df[["geography"]]).ravel()

    df["size_category"] = df["size_category"].apply(lambda x: x if x in size_category_encoder.classes_ else "Unknown")
    df["size_category"] = size_category_encoder.transform(df[["size_category"]]).ravel()

    processed_data = preprocessor.transform(df)

    feature_names = preprocessor.get_feature_names_out()
    cleaned_feature_names = [name.replace("num__", "") for name in feature_names]

    return pd.DataFrame(processed_data, columns=cleaned_feature_names, index=df.index)
