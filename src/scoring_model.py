from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import joblib

def train_model(X, y, save_path="model.pkl"):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    joblib.dump(model, save_path)
    return model

def predict_scores(model, X):
    raw_scores = model.predict(X)
    scaler = MinMaxScaler(feature_range=(0, 1000))
    final_scores = scaler.fit_transform(raw_scores.reshape(-1, 1)).flatten()
    return final_scores
