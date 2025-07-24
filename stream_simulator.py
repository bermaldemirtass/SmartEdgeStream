import time
import random
import json
from datetime import datetime

def generate_sensor_data():
    voltage = round(random.uniform(210, 230), 2)
    current = round(random.uniform(4, 6), 2)
    temperature = round(random.uniform(25, 35), 2)

    if random.random() < 0.05:
        voltage = round(random.uniform(150, 180), 2)
        current = round(random.uniform(10, 15), 2)
        temperature = round(random.uniform(50, 60), 2)

    power = round(voltage * current, 2)

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "voltage": voltage,
        "current": current,
        "temperature": temperature,
        "power": power
    }

if __name__ == "__main__":
    for _ in range(10):  # sadece 10 satır üret
        data = generate_sensor_data()
        print(json.dumps(data))
        time.sleep(1)

