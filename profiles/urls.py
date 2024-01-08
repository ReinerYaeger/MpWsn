from django.urls import path
from . import views
from .views import administrator

urlpatterns = [
	path('administrator/', views.index, name='index'),
	path('administrator/<str:username>/', administrator, name='user_profile'),
]
