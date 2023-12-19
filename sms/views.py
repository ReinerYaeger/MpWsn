from django.shortcuts import render

from iot import pi_files
from iot.pi_files.arduino_interface import get_serial_data

# Create your views here.

app_name = "sms"




def index(requests):
    get_serial_data()    

    context = {

    }
    return render(requests, 'sms/index.html', context)
