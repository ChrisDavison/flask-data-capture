from sqlalchemy import create_engine
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Measurement(Base):
    __tablename__ = "measurement"
    id: Mapped[int] = mapped_column(primary_key=True)
    sensor_id: Mapped[int] = mapped_column(ForeignKey("sensor.id"))
    sensor: Mapped["Sensor"] = relationship()
    datetime: Mapped[str] = mapped_column(String(30))
    co: Mapped[int]
    co2: Mapped[int]

    def __repr__(self) -> str:
        return f"Measurement(id={self.id!r}, sensor={self.sensor_id!r}, datetime='{self.datetime!r}', co='{self.co!r}', co2='{self.co2!r}')"


class Sensor(Base):
    __tablename__ = "sensor"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(30))
    location: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"SensorMetadata(id={self.id!r}, name='{self.name!r}', description='{self.description!r}', location='{self.location!r}')"


if __name__ == "__main__":
    engine = create_engine("sqlite:///sensors.db", echo=True)
    Base.metadata.create_all(engine)
