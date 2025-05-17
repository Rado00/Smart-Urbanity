from django.urls import path
from . import views

app_name = 'rado'

urlpatterns = [
    path('', views.home, name='home'),
] 