from flask import Flask, request
import json

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from createdb import Measurement, Sensor

app = Flask(__name__)
engine = create_engine("sqlite:///sensors.db", echo=True)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/save/<sensor>", methods=["POST"])
def save_sensor_data(sensor):
    # data = request.data.decode()
    # print(data)

    with Session(engine) as session:
        rows = []
        for row in json.loads(request.data.decode()):
            print(row)
            rows.append(
                Measurement(datetime=row["datetime"], co=row["co"], co2=row["co2"], sensor_id=sensor)
            )
        print(rows)
        session.add_all(rows)
        session.commit()
    return f"saved to sensor{sensor}!"


@app.route("/create_sensors", methods=["POST"])
def create_sensor():
    with Session(engine) as session:
        rows = []
        for row in json.loads(request.data.decode()):
            rowname = row["name"]
            got = session.execute(text(f"select name from sensor where name = '{rowname}'"))
            if got.fetchone():
                print("sensor already exists")
                continue
            print(f"Creating sensor: {rowname}")
            rows.append(
                Sensor(
                    name=row["name"],
                    description=row["description"],
                    location=row["location"],
                )
            )
        session.add_all(rows)
        session.commit()
    return "created sensor"


if __name__ == "__main__":
    app.run()
