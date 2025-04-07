import numpy as np
import pandas as pd

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    if {'rooms', 'sq_meters'}.issubset(df.columns):
        df['rooms_x_sqm'] = df['rooms'] * df['sq_meters']
        df['sqm_per_room'] = df['sq_meters'] / np.maximum(df['rooms'], 0.1)
    
    if {'no_of_bathrooms', 'sq_meters'}.issubset(df.columns):
        df['bathrooms_x_sqm'] = df['no_of_bathrooms'] * df['sq_meters']
        df['sqm_per_bathroom'] = df['sq_meters'] / np.maximum(df['no_of_bathrooms'], 0.1)
    
    if {'kitchens', 'livingRooms'}.issubset(df.columns):
        df['kitchen_living_ratio'] = df['kitchens'] / np.maximum(df['livingRooms'], 0.1)
    
    if {'rooms', 'no_of_bathrooms', 'kitchens', 'livingRooms'}.issubset(df.columns):
        df['total_rooms'] = df[['rooms', 'no_of_bathrooms', 'kitchens', 'livingRooms']].sum(axis=1)
        df['living_to_total_ratio'] = df['livingRooms'] / np.maximum(df['total_rooms'], 0.1)
        df['bathroom_to_room_ratio'] = df['no_of_bathrooms'] / np.maximum(df['rooms'], 0.1)
    
    if 'sq_meters' in df.columns:
        df['sq_meters_squared'] = df['sq_meters'] ** 2
        df['log_sq_meters'] = np.log1p(df['sq_meters'])
    
    if 'rooms' in df.columns:
        df['rooms_squared'] = df['rooms'] ** 2
    
    df['size_category'] = df['sq_meters'].apply(lambda x: categorize_size(x))
    
    return df

def categorize_size(sq_meters: float) -> str:
    if sq_meters < 50:
        return 'Very Small'
    elif sq_meters < 80:
        return 'Small'
    elif sq_meters < 120:
        return 'Medium'
    elif sq_meters < 180:
        return 'Large'
    return 'Very Large'

