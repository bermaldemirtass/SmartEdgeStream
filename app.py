import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="SmartEdgeStream", layout="wide")

st.title("🔌 SmartEdgeStream - Anomali Tespit Paneli")
st.markdown("Gerçek zamanlı enerji verileri için akıllı anomaly detection")

# Örnek veri
sample_data = [
    {"timestamp": "2025-07-23T21:01:01", "voltage": 220.5, "current": 5.2, "temperature": 30.1, "power": 1146.6},
    {"timestamp": "2025-07-23T21:01:02", "voltage": 219.3, "current": 5.5, "temperature": 29.8, "power": 1206.2},
    {"timestamp": "2025-07-23T21:01:03", "voltage": 175.2, "current": 12.1, "temperature": 55.1, "power": 2120.0},
    {"timestamp": "2025-07-23T21:01:04", "voltage": 225.8, "current": 5.0, "temperature": 30.5, "power": 1129.0},
    {"timestamp": "2025-07-23T21:01:05", "voltage": 228.4, "current": 4.7, "temperature": 31.2, "power": 1073.5},
    {"timestamp": "2025-07-23T21:01:06", "voltage": 180.0, "current": 11.5, "temperature": 52.3, "power": 2070.0},
    {"timestamp": "2025-07-23T21:01:07", "voltage": 221.7, "current": 5.3, "temperature": 30.0, "power": 1175.0},
    {"timestamp": "2025-07-23T21:01:08", "voltage": 230.0, "current": 4.9, "temperature": 29.9, "power": 1127.0},
    {"timestamp": "2025-07-23T21:01:09", "voltage": 223.2, "current": 5.1, "temperature": 30.4, "power": 1138.3},
    {"timestamp": "2025-07-23T21:01:10", "voltage": 155.0, "current": 13.0, "temperature": 58.0, "power": 2015.0}
]

df = pd.DataFrame(sample_data)

# Pipeline
features = df[['voltage', 'current', 'temperature', 'power']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

model = IsolationForest(contamination=0.2, random_state=42)
df['anomaly'] = model.fit_predict(X_scaled)
df['anomaly'] = df['anomaly'].map({1: 'normal', -1: 'anomaly'})

# Görsel tablo
st.dataframe(df, use_container_width=True)

# Sayım
anomaly_count = (df['anomaly'] == 'anomaly').sum()
st.metric("🚨 Tespit Edilen Anomaliler", anomaly_count)

