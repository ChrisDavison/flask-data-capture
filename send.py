import requests
import datetime
import random


data = [{"name": "Science Centre", "description": "Under gantry", "location": "Clyde"}]
create_sensors = requests.post("http://localhost:5000/create_sensors", json=data)


data = []
for i in range(100):
    timestamp = datetime.datetime.now().isoformat()
    co = random.randint(0, 10)
    co2 = random.randint(0, 100)
    data.append({"datetime": timestamp, "co": co, "co2": co2})
requests.post("http://localhost:5000/save/2", json=data)
