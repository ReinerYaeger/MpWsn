from django.urls import path
from django.contrib.auth.views import LoginView
from .views import index, continuous_data_retrieval_api, get_updated_data, search_view, page1, charts, CustomLoginView, \
    SignupView, setup

urlpatterns = [
    path('', index, name='index'),
    path('soil_moisture_data/', continuous_data_retrieval_api, name='continuous_retrieval'),
    path('get_updated_data/', get_updated_data, name='get_updated_data'),
    path('search/', search_view, name='search'),
    path('charts/', charts, name='charts'),
    path('myview/', page1, name="page1"),
    path('login/', CustomLoginView.as_view(success_url='sms/page1/'), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('setup/',setup, name='setup'),
]
