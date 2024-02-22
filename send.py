import requests
import datetime
import random


data = []
for i in range(100):
    timestamp = datetime.datetime.now().isoformat()
    co = random.randint(0, 10)
    co2 = random.randint(0, 100)
    data.append({'datetime': timestamp, 'co': co, 'co2': co2})

requests.post('http://localhost:8000/save/1', json=data)
