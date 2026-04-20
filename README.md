# Praktikum 7 - Machine Learning untuk Prediksi Traffic (Smart City AI)

## Identitas
- **Nama**: Muhammad Nur Ihsan
- **NIM**: 230104040214
- **Mata Kuliah**: Big Data Technology
- **Dosen**: Muhayat, M.IT
- **Universitas**: UIN Antasari Banjarmasin

---

## Deskripsi Project
Project ini mengimplementasikan Machine Learning (Random Forest) untuk memprediksi jumlah kendaraan berdasarkan data traffic Smart City. Pipeline mencakup data cleaning, feature engineering, modeling, dan dashboard interaktif menggunakan Streamlit.

---

## Teknologi yang Digunakan
- Python 3.12
- Pandas
- Scikit-learn (Random Forest)
- Joblib
- Streamlit
- Matplotlib

---

## Struktur File
projectbigdata7_230104040214/
├── traffic_smartcity_v1.csv          # Dataset raw
├── traffic_smartcity_clean_v1.csv    # Dataset setelah cleaning
├── traffic_data_cleaning_v1.py       # Script data cleaning
├── traffic_ml_model_v1.py            # Script ML modeling
├── traffic_dashboard_v1.py           # Dashboard Streamlit
└── traffic_model_v1.pkl              # Model tersimpan

---

## Cara Menjalankan

### 1. Install library
pip install pandas scikit-learn joblib streamlit matplotlib

### 2. Jalankan Data Cleaning
python traffic_data_cleaning_v1.py

### 3. Jalankan ML Model
python traffic_ml_model_v1.py

### 4. Jalankan Dashboard
streamlit run traffic_dashboard_v1.py

---

## Hasil
- **Dataset**: 168 baris data traffic kendaraan
- **Model**: Random Forest Regressor
- **Fitur**: Hour, Day, Lag1
- **Metrik Evaluasi**: MAE (Mean Absolute Error)

---

## Pipeline
data raw → data cleaning → feature engineering → modeling → dashboard → insight
