from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *

# Create your views here.
class Base(View):
	context = {}


class HomeView(Base):
	def get(self,request):

		return render(request,'index.html',self.context)



class ExchangeView(Base):
	def get(self,request):
		return render(request,'exchange.html',self.context)