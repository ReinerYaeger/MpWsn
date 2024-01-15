# Code for the Raspberry pi
import asyncio
import pickle
import threading
from time import sleep
import serial
import traceback
from datetime import datetime
import logging
import socket
import random

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', filename='mp_wn.log', encoding='utf-8',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)
file_path = "sensor_location.txt"


def get_random_data_from_file():
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            random_line = random.choice(lines)

            sensor_group_name, Parish, lat, lng = random_line.strip().split(', ')

            return {
                'sensor_group_name': sensor_group_name,
                'Parish': Parish,
                'lat': float(lat),
                'lng': float(lng),
            }
    except FileNotFoundError:
        print(f"The file '{file_path}' is not present.")
    except Exception as e:
        print(f"An unexpected error occurred while reading random data from the file: {e}")


def write_data_to_file(data):
    try:
        with open(file_path, "a") as file1:
            file1.write(','.join(data) + '\n')
        print("Data written to the file.")
    except FileNotFoundError:
        print(f"The file '{file_path}' is not present. Creating the file...")
        with open(file_path, "w") as file1:
            file1.write(','.join(data) + '\n')
        print(f"The file '{file_path}' has been created with initial data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def delete_data_from_file(data):
    try:
        lines = []
        with open(file_path, "r") as file1:
            lines = file1.readlines()

        with open(file_path, "w") as file1:
            for line in lines:
                if line.strip("\n") != ','.join(data):
                    file1.write(line)

        print(f"Data '{','.join(data)}' deleted from the file.")

    except FileNotFoundError:
        print(f"The file '{file_path}' is not present. Creating the file...")
        with open(file_path, "w") as file1:
            file1.write(','.join(data) + '\n')
        print(f"The file '{file_path}' has been created with initial data.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def get_serial_data(sleep_sec=0):
    try:
        ser = serial.Serial('COM7', 9600, timeout=1)
        ser.flushInput()

        analog_dict = {
            'A0': {'sensor_group': None, 'parish': None, 'lat': None, 'lng': None, 'soil_moisture_data': [],
                   'timestamp': []},
            'A1': {'sensor_group': None, 'parish': None, 'lat': None, 'lng': None, 'soil_moisture_data': [],
                   'timestamp': []},
            'A2': {'sensor_group': None, 'parish': None, 'lat': None, 'lng': None, 'soil_moisture_data': [],
                   'timestamp': []},
        }

        while True:
            ser_bytes = ser.readline()
            decoded_string = ser_bytes.decode("utf-8").strip()

            if decoded_string and decoded_string != "":
                output_list = decoded_string.split("\t")
                for data_point in output_list:
                    for prefix in ['A0:', 'A1:', 'A2:']:
                        if prefix in data_point:
                            # Use random data from the file
                            random_data = get_random_data_from_file()

                            # Update analog_dict with random data
                            analog_dict[prefix[:-1]]['sensor_group'] = random_data['sensor_group_name']
                            analog_dict[prefix[:-1]]['parish'] = random_data['Parish']
                            analog_dict[prefix[:-1]]['lat'] = random_data['lat']
                            analog_dict[prefix[:-1]]['lng'] = random_data['lng']

                            data_value = data_point.split(":")[1].strip()
                            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            data_dict = {
                                'soil_moisture_data': data_value,
                                'timestamp': timestamp
                            }
                            if data_value:
                                analog_dict[prefix[:-1]]['soil_moisture_data'] = data_dict['soil_moisture_data']
                                analog_dict[prefix[:-1]]['timestamp'] = data_dict['timestamp']

            # process_data(analog_dict)
            print(analog_dict)
            # logging.info(analog_dict)

            sleep(sleep_sec)

    except KeyboardInterrupt as e:
        logging.error(f"Keyboard Interrupt {e}")
        logging.error(traceback.print_exc())

    except serial.SerialTimeoutException as e:
        logging.error(f"Serial Timeout Exception: {e}")
        logging.error(traceback.print_exc())

    except serial.SerialException as e:
        logging.error(f"SerialException caught: {e}")
        logging.error(traceback.print_exc())

    except PermissionError as pe:
        logging.critical(f"Permission Error: {pe}")
        logging.error(traceback.print_exc())

    except TypeError as e:
        logging.error(f"Possible Sensor Disconnection\tType Error {e}")
        logging.error(traceback.print_exc())

    except Exception as ex:
        logging.error(f"An unexpected error occurred: {ex}")
        logging.error(traceback.print_exc())


def process_data(analog_dict):
    try:
        encoded_data = pickle.dumps(analog_dict)
        # send_data(encoded_data)
        asyncio.run(send_data_async(encoded_data))
        logging.info(f"Data contents {analog_dict} ")
    except Exception as e:
        logging.error(e)


def send_data(data):
    host = "127.0.0.1"
    port = 1234

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(data)
    except socket.error as e:
        logger.error(f"Socket Error: {e}")
    return


async def send_data_async(data):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 1234)

    writer.write(data)
    await writer.drain()
    logging.info(f"Data Sent {data}")
    writer.close()
    await writer.wait_closed()


# def encrypt_data(token):
#     load_dotenv()
#     f = Fernet(os.getenv("KEY"))
#     token = base64.b64encode(str(token).encode('utf-8')).decode('utf-8')
#     encrypted_token = f.encrypt(token.encode())
#     return encrypted_token
#
#
# def decrypt_data(en_byte):
#     load_dotenv()
#     f = Fernet(os.getenv("KEY"))
#     decrypted_token = f.decrypt(en_byte)
#     return base64.b64decode(decrypted_token.decode())


def main():
    get_serial_data()


def listening_server():
    host = '127.0.0.1'
    port = 1234

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        # Handle client communication in a separate thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


def handle_client(client_socket):
    try:
        # Handle communication with the connected client
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            else:
                for key, csv_values in data.items():
                    values_list = [value.strip() for value in csv_values.split(',')]

                if values_list[0].lower() == 'write':
                    write_data_to_file(values_list[1:])
                elif values_list[0].lower() == 'delete':
                    delete_data_from_file(values_list[1:])
                else:
                    print(f"Invalid instruction: {values_list[0]}")

    except Exception as e:
        logging.error(f"Error handling client: {e}")
    finally:
        client_socket.close()
        print("Client disconnected")


if __name__ == '__main__':
    try:
        threading.Thread(target=listening_server).start()
    except Exception as e:
        logging.error(e)

    #get_serial_data()
    # main()
