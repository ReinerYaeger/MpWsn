from django.db import models
from django.contrib.gis.db import models as gis_model
from sqlalchemy.orm import sessionmaker, declarative_base

# from django.contrib.gis.db import models as gis_model

Base = declarative_base()


# class SoilSensorData(models.Model):
#     sensor_name = models.CharField(max_length=255)
#     sensor_data = models.FloatField()
#     sensor_date_time = models.DateTimeField(primary_key=True)
#
#     class Meta:
#         db_table = 'soil_sensor_data'


class LocationSoilSensorData(gis_model.Model):
    ID = gis_model.AutoField(primary_key=True, null=False)
    sensor_name = gis_model.CharField(max_length=255)
    sensor_group_name = gis_model.CharField(max_length=255)
    sensor_data = gis_model.FloatField()
    sensor_date_time = gis_model.DateTimeField(null=False)
    creation_date = gis_model.DateTimeField(null=False)
    parish = gis_model.CharField(max_length=10)
    geo_location = gis_model.PointField()

    def __str__(self):
        return self.sensor_group_name

    class Meta:
        db_table = 'location_soil_sensor_data'
        verbose_name_plural = 'location_soil_sensor_data'

# class SoilMoistureLevels(gis_model.Model):
#     id = gis_model.IntegerField(primary_key=True)
#     location = gis_model.CharField(max_length=150)
#     soil_moisture_data_historical = gis_model.DecimalField(max_digits=5)
#     creation_date = gis_model.DateTimeField()
#     gps = gis_model.PointField()
#
#     def __str__(self):
#         return self.location
#
#     class Meta:
#         verbose_name_plural = 'SoilMoistureLevels'


# class SoilSensorData(Base):
#     __tablename__ = 'soil_sensor_data'
#
#     sensor_name = Column(String)
#     sensor_data = Column(Float)
#     sensor_date_time = Column(DateTime, primary_key=True)
