from django.db import models
from sqlalchemy import create_engine, select, desc, Column, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class SoilSensorData(Base):
    __tablename__ = 'soil_sensor_data'

    sensor_name = Column(String)
    sensor_data = Column(Float)
    sensor_date_time = Column(DateTime, primary_key=True)
