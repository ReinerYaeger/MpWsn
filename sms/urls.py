from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from pi_talk import urls
from profiles.views import administrator
from .views import index, experiment, live_analytics, experiment_results

urlpatterns = [
	path('', index, name='index'),
	path('/live_analytics', live_analytics, name='live_analytics'),
	path('/experiment_results', experiment_results, name='experiment_results'),
	path('/experiment', experiment, name='experiment'),
	path('/administrator', administrator, name="administrator"),

	# path('soil_moisture_data/', continuous_data_retrieval_api, name='continuous_retrieval'),
	# path('get_updated_data/', get_updated_data, name='get_updated_data'),
	# path('charts/', charts, name='charts'),
	# path('accounts/login/', LoginView.as_view(template_name='sms/login.html'), name='login'),
	# path('logout/', CustomLogoutView.as_view(), name='logout'),
	# path('signup/', signup_view, name='signup'),
	# path('setup/', setup, name='setup'),
]

