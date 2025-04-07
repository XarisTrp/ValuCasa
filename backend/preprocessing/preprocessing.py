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
