import logging
from mysql.connector import connect, Error
import asyncio

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', filename='mp_wn.log', encoding='utf-8',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

try:
    connection = connect(
        host="localhost",
        user="root",
        password="",
        database="mp_wsn"

    )
    logger.info("Connected to the database")
    print("Connected to the database")

except Error as e:
    logger.error("Error connecting to the database: %s", e)
except Exception as e:
    logger.error("Database connection error: %s", str(e))

data_dict = {
    'A0': [],
    'A1': [],
    'A2': [],
}


async def algoriddim():
    analog_dict = {
        'A0': {'soil_moisture_data': [], 'timestamp': []},
        'A1': {'soil_moisture_data': [], 'timestamp': []},
        'A2': {'soil_moisture_data': [], 'timestamp': []},
    }
    while True:
        await asyncio.sleep(1)
        if len(analog_dict['A0']) < 200:
            connection.cursor().execute(f"""SELECT * FROM soil_sensor_data ORDER BY sensor_data_time DESC LIMIT 200""")
            query_result = connection.cursor().fetchall()
            for row in query_result:
                sensor_name = row[0]
                sensor_data = row[1]
                sensor_data_time = row[2]

                analog_dict[sensor_name]['soil_moisture_data'].append(sensor_data)
                analog_dict[sensor_name]['timestamp'].append(sensor_data_time)

        if len(analog_dict['A0']) == 200:
            print(analog_dict['A0']['soil_moisture_data'].index(len(analog_dict['A0']['soil_moisture_data'])))
            connection.cursor().execute(f"""SELECT * FROM soil_sensor_data ORDER BY sensor_data_time DESC LIMIT 1""")


def anova_test():
    connection.cursor().execute(
        f"""SELECT sensor_name,sensor_data FROM soil_sensor_data ORDER BY sensor_name DESC LIMIT 150""")

    for row in connection.cursor().fetchall():
        sensor_name = row[0]
        sensor_data = row[1]

        data_dict[sensor_name].append(sensor_data)
        print(data_dict)

    sensor_data = connection.cursor().fetchall()

    return


def main():
    anova_test()
    return


if __name__ == '__main__':
    main()
