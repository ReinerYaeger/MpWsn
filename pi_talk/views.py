from django.shortcuts import render

from sms.pi_server import start_server
server_running = bool

# Create your views here.
if not server_running:
    start_server()
    server_running = True
def index(requests):

    context = {

    }
    return render(requests, 'sms/index.html', context)