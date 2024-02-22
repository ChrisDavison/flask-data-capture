from flask import Flask, request
import json

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from createdb import Measurement

app = Flask(__name__)
engine = create_engine('sqlite:///sensors.db', echo=True)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/save/<sensor>', methods=['POST'])
def save_sensor_data(sensor):
    # data = request.data.decode()
    # print(data)

    with Session(engine) as session:
        rows = []
        for row in json.loads(request.data.decode()):
            print(row)
            rows.append(Measurement(
                datetime=row['datetime'],
                co=row['co'],
                co2=row['co2']
            ))
        session.add_all(rows)
        session.commit()
    return f'saved to sensor{sensor}!'


if __name__ == '__main__':
    app.run()
