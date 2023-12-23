from django.shortcuts import render
from iot.pi_files import arduino_interface
from iot.pi_files import server
from threading import Thread

# Create your views here.


def index(requests):

    try:
        t2 = Thread(target=arduino_interface.get_serial_data())
        context = {
        }

        t2.start()
    except Exception as e:
        print("Error starting threads:", e)


    return render(requests, 'sms/index.html', context)
