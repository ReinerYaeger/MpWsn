import threading
import time
import logging
from sqlalchemy import create_engine, select, desc, Column, String, Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from collections import deque

Base = declarative_base()
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', filename='../iot/pi_files/mp_wn.log', encoding='utf-8',
                    level=logging.DEBUG)


class SoilSensorData(Base):
    __tablename__ = 'soil_sensor_data'

    sensor_name = Column(String)
    sensor_data = Column(Float)
    sensor_date_time = Column(DateTime, primary_key=True)


engine = create_engine('mysql+mysqlconnector://root:@localhost/mp_wsn', pool_recycle=3600)
Session = sessionmaker(bind=engine)
session = Session()


def initial_retrieval(analog_dict):
    query = (
        select(SoilSensorData.sensor_name, SoilSensorData.sensor_data, SoilSensorData.sensor_date_time)
        .filter(SoilSensorData.sensor_name.in_(['A0', 'A1', 'A2']))
        .order_by(desc(SoilSensorData.sensor_date_time))
        .limit(5)
    )

    query_result = session.execute(query)

    for row in query_result:
        sensor_name = row[0]
        sensor_data = row[1]
        sensor_date_time = row[2].strftime('%Y-%m-%d %H:%M:%S')

        analog_dict[sensor_name]['soil_moisture_data'].append(sensor_data)
        analog_dict[sensor_name]['timestamp'].append(sensor_date_time)


def continuous_update(analog_dict):
    query = (
        select(SoilSensorData.sensor_name, SoilSensorData.sensor_data, SoilSensorData.sensor_date_time)
        .filter(SoilSensorData.sensor_name.in_(['A0', 'A1', 'A2']))
        .order_by(desc(SoilSensorData.sensor_date_time))
        .limit(1)
    )

    query_result = session.execute(query)

    for row in query_result:
        sensor_name = row[0]
        sensor_data = row[1]
        sensor_date_time = row[2].strftime('%Y-%m-%d %H:%M:%S')

        if len(analog_dict[sensor_name]['soil_moisture_data']) >= 5:
            analog_dict[sensor_name]['soil_moisture_data'].popleft()
            analog_dict[sensor_name]['timestamp'].popleft()
        analog_dict[sensor_name]['soil_moisture_data'].append(sensor_data)
        analog_dict[sensor_name]['timestamp'].append(sensor_date_time)


def continuous_data_retrieval(analog_dict,data_queue):

    while True:
        if len(analog_dict['A0']['soil_moisture_data']) < 5:
            initial_retrieval(analog_dict)

        if len(analog_dict['A0']['soil_moisture_data']) == 5:
            continuous_update(analog_dict)

        data_queue.put(analog_dict)
        time.sleep(3)


def main():
    threading.Thread(target=continuous_data_retrieval).start()
    return


if __name__ == '__main__':
    main()
