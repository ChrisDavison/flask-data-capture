from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session



class Base(DeclarativeBase):
    pass


class Measurement(Base):
    __tablename__ = 'measurements'
    id: Mapped[int] = mapped_column(primary_key=True)
    datetime: Mapped[datetime] = mapped_column(String(30))
    co: Mapped[int]
    co2: Mapped[int]

    def __repr__(self) -> str:
        return f"Measurement(id={self.id!r}, datetime='{self.datetime!r}', co='{self.co!r}', co2='{self.co2!r}')"


if __name__ == '__main__':
    engine = create_engine('sqlite:///sensors.db', echo=True)
    Base.metadata.create_all(engine)
