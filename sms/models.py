from django.db import models
from sqlalchemy import create_engine, select, desc, Column, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class SoilSensorData(models.Model):
    sensor_name = models.CharField(max_length=255)
    sensor_data = models.FloatField()
    sensor_date_time = models.DateTimeField(primary_key=True)

    class Meta:
        db_table = 'soil_sensor_data'

# class SoilSensorData(Base):
#     __tablename__ = 'soil_sensor_data'
#
#     sensor_name = Column(String)
#     sensor_data = Column(Float)
#     sensor_date_time = Column(DateTime, primary_key=True)
