from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Means home page, goes into views.py to take the function index and does what its there
]