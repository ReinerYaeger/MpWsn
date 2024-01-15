from django.urls import path
from .views import administrator,index

urlpatterns = [
	path('administrator/', index, name='index'),
	path('administrator/<str:username>/', administrator, name='user_profile'),
]