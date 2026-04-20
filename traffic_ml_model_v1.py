import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

df = pd.read_csv('data/clean/traffic_smartcity_clean_v1.csv')

df['datetime'] = pd.to_datetime(df['datetime'])
df['hour'] = df['datetime'].dt.hour
df['day'] = df['datetime'].dt.dayofweek
df['lag1'] = df['traffic'].shift(1)
df = df.dropna()

X = df[['hour', 'day', 'lag1']]
y = df['traffic']

model = RandomForestRegressor()
model.fit(X, y)

pred = model.predict(X)
mae = mean_absolute_error(y, pred)

print(f"Model berhasil dilatih!")
print(f"MAE: {mae:.2f}")

joblib.dump(model, 'models/traffic_model_v1.pkl')
print("Model berhasil disimpan di: models/traffic_model_v1.pkl")
