from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import index, continuous_data_retrieval_api, get_updated_data, charts, setup, signup_view, CustomLogoutView

urlpatterns = [
	path('', index, name='index'),
	path('soil_moisture_data/', continuous_data_retrieval_api, name='continuous_retrieval'),
	path('get_updated_data/', get_updated_data, name='get_updated_data'),
	path('charts/', charts, name='charts'),
	path('accounts/login/', LoginView.as_view(template_name='sms/login.html'), name='login'),
	path('logout/', CustomLogoutView.as_view(), name='logout'),
	path('signup/', signup_view, name='signup'),
	path('setup/', setup, name='setup'),
]
