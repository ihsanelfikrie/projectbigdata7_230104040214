import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Traffic AI", layout="wide")

st.title("🚦 Smart City Traffic Dashboard")
st.markdown("**Praktikum 7 — Machine Learning untuk Prediksi Traffic**")

# Load data & model
df = pd.read_csv('data/clean/traffic_smartcity_clean_v1.csv')
model = joblib.load('models/traffic_model_v1.pkl')

# Feature engineering
df['datetime'] = pd.to_datetime(df['datetime'])
df['hour'] = df['datetime'].dt.hour
df['day'] = df['datetime'].dt.dayofweek
df['lag1'] = df['traffic'].shift(1)
df = df.dropna()

# Metrics
st.subheader("📈 Statistik Traffic")
col1, col2, col3 = st.columns(3)
col1.metric("Avg Traffic", int(df['traffic'].mean()))
col2.metric("Max Traffic", int(df['traffic'].max()))
col3.metric("Min Traffic", int(df['traffic'].min()))

# Chart
st.subheader("📉 Traffic Trend")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df['traffic'].values, color='steelblue')
ax.set_xlabel("Waktu")
ax.set_ylabel("Jumlah Kendaraan")
ax.set_title("Tren Traffic Kendaraan")
st.pyplot(fig)

# Prediction
st.subheader("🔮 Prediksi Traffic")
col4, col5, col6 = st.columns(3)
hour = col4.slider("Jam", 0, 23, 17)
day = col5.slider("Hari (0=Senin)", 0, 6, 2)
lag1 = col6.number_input("Traffic Sebelumnya", 50, 300, 120)

if st.button("Prediksi"):
    pred = model.predict([[hour, day, lag1]])
    st.success(f"🚗 Prediksi: {int(pred[0])} kendaraan")
