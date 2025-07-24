🔌 SmartEdgeStream

SmartEdgeStream is a real-time machine learning pipeline that simulates sensor data from edge devices and detects anomalies using Isolation Forest. The project emulates real-world energy monitoring systems and offers a lightweight, stream-ready solution with a user-friendly dashboard.


 🚀 Features

- 📡 Real-time sensor data simulation (`stream_simulator.py`)
- 🧠 ML-based anomaly detection pipeline (`pipeline.py`)
- 🧪 Feature engineering and normalization
- 📊 Streamlit-powered interactive dashboard (`app.py`)
- ✅ Deployable structure for IoT/Edge use cases
- 💡 Lightweight and entirely written in Python


🔧 Technologies Used

- Python 3.9+
- Pandas, NumPy
- Scikit-learn (Isolation Forest)
- Streamlit (Dashboard UI)
- JSON for data representation
- (Optional: Docker for deployment)


💻 How to Run

1. Install dependencies

```bash
pip install -r requirements.txt

2. Run the sensor stream simulator (generates example data)

python stream_simulator.py

3. Run the machine learning pipeline to process and label the data

python pipeline.py

4. Launch the Streamlit dashboard to visualize anomalies

streamlit run app.py

💡 Tip: For demo purposes, stream_simulator.py is limited to 10 entries for quick testing. You can modify the loop for continuous streaming.

 📷 Dashboard Preview

> Example output from the real-time anomaly detection interface:

![SmartEdgeStream UI](https://github.com/bermaldemirtass/SmartEdgeStream/blob/main/assets/dashboard.png?raw=true)

