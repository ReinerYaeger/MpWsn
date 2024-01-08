import socket
import pickle
import logging
from mysql.connector import connect, Error
import asyncio

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', filename='../iot/pi_files/mp_wn.log', encoding='utf-8',
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


async def data_handler(reader, writer):
    data = await reader.read(4096)

    rec_data = pickle.loads(data)
    addr = writer.get_extra_info('peername')
    logging.info(f"Connection from {addr} Data :{rec_data}")

    writer.close()
    await writer.wait_closed()

    upload_data(rec_data)


async def server_async():
    server = await asyncio.start_server(
        data_handler, '127.0.0.1', 1234)

    addr = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()


def server():
    HOST = '0.0.0.0'  # Listen on all available interfaces
    PORT = 1234
    # connection = define_connection()

    try:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()

            logging.debug(f"Server listening on port {PORT}...")

            while True:
                conn, addr = s.accept()
                logging.info(f"Connected by {addr}")
                data = conn.recv(4096)
                rec_data = pickle.loads(data)
                logging.info(f"Data by {rec_data}")
                upload_data(rec_data)

    except socket.error as e:
        logging.error(f"{e}")
    except Exception as e:
        logging.critical(f"{e}")


def upload_data(data):
    for item in data:
        sensor_name = str(item)
        sensor_data = data[f'{sensor_name}']['soil_moisture_data']
        sensor_date_time = data[f'{sensor_name}']['timestamp']

        logging.debug(f"Processing sensor: {sensor_name}")
        logging.debug(f"Sensor data: {sensor_data}")
        logging.debug(f"Sensor date/time: {sensor_date_time}")

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO soil_sensor_data(sensor_name, sensor_data, sensor_date_time) VALUES (%s, %s, %s)"
                values = (sensor_name, sensor_data, sensor_date_time)
                cursor.execute(sql, values)

            connection.commit()  # Commit after each successful insertion
            print("Data inserted for sensor: %s %s", sensor_name, sensor_data)
            logging.debug("Data inserted for sensor: %s %s", sensor_name, sensor_data)
        except Exception as err:
            logging.error("Unexpected error for sensor %s: %s", sensor_name, err)


def main():
    asyncio.run(server_async())
    # server()


if __name__ == "__main__":
    main()
