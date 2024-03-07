from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import index, experiment, live_analytics, environmental_statistics, map_view, sensor_dataset, administrator, \
    report

urlpatterns = [
    path('', index, name='index'),
    path('live_analytics/', live_analytics, name='live_analytics'),
    path('environmental_statistics/', environmental_statistics, name='environmental_statistics'),
    path('experiment/', experiment, name='experiment'),
    path('administrator/',administrator,name="administrator" ),
    path('map_view', map_view, name="map_view"),
    path('map_view/<str:parish>', map_view, name="map_view"),
    path('sensor_dataset/', sensor_dataset, name='sensor_dataset'),
    path('report/', report, name='report'),

    # path('soil_moisture_data/', continuous_data_retrieval_api, name='continuous_retrieval'),
    # path('get_updated_data/', get_updated_data, name='get_updated_data'),
    # path('charts/', charts, name='charts'),
    # path('accounts/login/', LoginView.as_view(template_name='sms/login.html'), name='login'),
    # path('logout/', CustomLogoutView.as_view(), name='logout'),
    # path('signup/', signup_view, name='signup'),
    # path('setup/', setup, name='setup'),
]
