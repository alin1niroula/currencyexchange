from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views



urlpatterns = [
path('', HomeView.as_view(), name='home'),
path('exchange', ExchangeView.as_view(), name='exchange'),

]