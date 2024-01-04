from django.urls import path
from . import views
from .views import user_profile

urlpatterns = [
	path('profile/', views.index, name='index'),
	path('profile/<str:username>/', user_profile, name='user_profile'),
]
