import pandas as pd

df = pd.read_csv('data/raw/traffic_smartcity_v1.csv')

print("=== Data Sebelum Cleaning ===")
print(f"Jumlah baris: {len(df)}")
print(f"Kolom: {df.columns.tolist()}")
print(df.head())

df['datetime'] = pd.to_datetime(df['datetime'])
df = df.sort_values('datetime')
df = df.dropna()

print("\n=== Data Setelah Cleaning ===")
print(f"Jumlah baris: {len(df)}")

df.to_csv('data/clean/traffic_smartcity_clean_v1.csv', index=False)

print("Data cleaning selesai!")
print("File tersimpan di: data/clean/traffic_smartcity_clean_v1.csv")
