# src/preprocess.py
import pandas as pd

def preprocess(df):
    """
    Preprocess the raw dataframe and return features and target.
    """
    # Copy to avoid modifying original
    df = df.copy()
    
    # Drop any missing values
    df = df.dropna()

    # Define features and target
    features = ['Near_Location', 'Promo_friends', 'Contract_period',
                'Month_to_end_contract', 'Lifetime', 'Avg_class_frequency_total', 'Partner']
    X = df[features]
    y = df['Churn']
    
    return X, y
