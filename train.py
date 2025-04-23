import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

df = pd.read_csv('data/data.csv')
X = df[['feature']]
y = df['target']

model = LinearRegression().fit(X, y)
os.makedirs('model', exist_ok=True)
joblib.dump(model, 'model/model.pkl')
print("Model saved.")
