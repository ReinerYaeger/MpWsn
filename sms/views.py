import random
import threading
from time import sleep

from bokeh.embed import components
from bokeh.plotting import figure
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import JsonResponse, request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView
from sqlalchemy.orm import declarative_base

from sms.forms import SignupForm


class DataGenerator:
	def __init__(self):
		self.x = []
		self.y = []

	def gen_data(self):
		while True:
			self.x.append(random.randint(0, 150))
			self.y.append(random.randint(0, 150))
			sleep(5)


dg = DataGenerator()


def index(request):
	return render(request, 'sms/index.html')


def get_updated_data(request):
	# Access the x and y values from the DataGenerator instance
	data = {
		'x': dg.x,
		'y': dg.y,
	}

	return JsonResponse(data)


shared_data = {}
lock = threading.Lock()


def page1(request):
	return render(request, 'sms/index.html')


def charts(request):
	# Start the data generation in a separate thread
	import threading
	data_thread = threading.Thread(target=dg.gen_data)
	data_thread.daemon = True  # Set the thread as daemon so it stops when the main thread stops
	data_thread.start()

	# Prepare initial plot without data
	title = 'y = f(x)'
	plot = figure(
		title=title,
		x_axis_label='X-Axis',
		y_axis_label='Y-Axis',
		width=400,
		height=400
	)
	line = plot.line(dg.x, dg.y, legend_label='f', line_width=2)
	script, div = components(plot)
	context = {
		'script': script,
		'div': div,
	}
	return render(request, 'sms/technique/charts.html', context)


class CustomLoginView(LoginView):
	template_name = 'sms/login.html'

	def form_valid(self, form):
		"""If the form is valid, perform login and redirect."""
		login(self.request, form.get_user())
		return redirect('index')  # Adjust the redirect URL

	def form_invalid(self, form):
		"""If the form is invalid, render the invalid form."""
		return self.render_to_response(self.get_context_data(form=form))


class CustomLogoutView(LogoutView):
	next_page = reverse_lazy('index')

	def get_next_page(self):
		return self.next_page

	def dispatch(self, requests, *args, **kwargs):
		super().dispatch(requests, *args, **kwargs)
		return redirect(request, 'sms/index')


def signup_view(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			# Redirect to a success page or login page
			return redirect('login')  # You can adjust the redirect URL
	else:
		form = SignupForm()

	return render(request, 'sms/signup.html', {'form': form})


def setup(requests):
	return render(requests, 'sms/setup/setup.html')


@csrf_protect
def continuous_data_retrieval_api(request):
	Base = declarative_base()

# def queue_to_list(q):
#     return list(q.queue)
#
# class SoilSensorData(Base):
#     __tablename__ = 'soil_sensor_data'
#
#     sensor_name = Column(String)
#     sensor_data = Column(Float)
#     sensor_date_time = Column(DateTime, primary_key=True)
#
# engine = create_engine('mysql+mysqlconnector://root:@localhost/mp_wsn', pool_recycle=3600)
# Session = sessionmaker(bind=engine)
# session = Session()
#
# analog_dict = {
#     'A0': {'soil_moisture_data': Queue(maxsize=5), 'timestamp': Queue(maxsize=5)},
#     'A1': {'soil_moisture_data': Queue(maxsize=5), 'timestamp': Queue(maxsize=5)},
#     'A2': {'soil_moisture_data': Queue(maxsize=5), 'timestamp': Queue(maxsize=5)},
# }
#
# query = (
#     select(SoilSensorData.sensor_name, SoilSensorData.sensor_data, SoilSensorData.sensor_date_time)
#     .filter(SoilSensorData.sensor_name.in_(['A0', 'A1', 'A2']))
#     .order_by(desc(SoilSensorData.sensor_date_time))
#     .limit(1)
# )
#
# query_result = session.execute(query)
#
# for row in query_result:
#     sensor_name = row[0]
#     sensor_data = row[1]
#     sensor_date_time = row[2].strftime('%Y-%m-%d %H:%M:%S')
#
#     if analog_dict[sensor_name]['soil_moisture_data'].qsize() >= 5:
#         analog_dict[sensor_name]['soil_moisture_data'].get()
#         analog_dict[sensor_name]['timestamp'].get()
#     analog_dict[sensor_name]['soil_moisture_data'].put(sensor_data)
#     analog_dict[sensor_name]['timestamp'].put(sensor_date_time)
#
#     print(f'A0  {analog_dict["A0"]["soil_moisture_data"]} {analog_dict["A0"]["timestamp"]}')
#     print(f'A1  {analog_dict["A1"]["soil_moisture_data"]} {analog_dict["A1"]["timestamp"]}')
#     print(f'A2  {analog_dict["A2"]["soil_moisture_data"]} {analog_dict["A2"]["timestamp"]}')
#
# return JsonResponse({'soil_moisture_data': serializable_dict})
