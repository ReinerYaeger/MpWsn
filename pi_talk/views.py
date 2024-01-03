from django.shortcuts import render

from pi_server import start_server
from  threading import Thread

server_running = bool

# Create your views here.
if not server_running:
    thread = Thread(target=start_server())
    thread.start()
    server_running = True


def index(requests):
    context = {

    }
    return render(requests, 'sms/login.html', context)
