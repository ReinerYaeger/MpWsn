from django.shortcuts import render

from iot.pi_files import arduino_interface
from threading import Thread

# Create your views here.


def index(requests):
    a_i_thread = Thread(target=arduino_interface.get_serial_data())
    a_i_thread.start()

    context = {

    }

    return render(requests, 'sms/index.html', context)
