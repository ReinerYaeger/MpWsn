from django.urls import path
from .views import index, continuous_data_retrieval_api, get_updated_data

urlpatterns = [
    path('', index, name='index'),
    path('soil_moisture_data/', continuous_data_retrieval_api, name='continuous_retrieval'),
    path('get_updated_data/', get_updated_data, name='get_updated_data'),
]
