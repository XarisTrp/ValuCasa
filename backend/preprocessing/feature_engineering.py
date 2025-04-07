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

