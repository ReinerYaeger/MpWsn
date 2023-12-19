from django.shortcuts import render

from iot.pi_files import arduino_interface
from . import pi_server
from threading import Thread

# Create your views here.


def index(requests):

    server_thread = Thread(target=pi_server.start_server)
    server_thread.start()

    a_i_thread = Thread(target=arduino_interface.get_serial_data())
    a_i_thread.start()

    context = {

    }

    return render(requests, 'sms/index.html', context)
