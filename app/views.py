from time import strftime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
import os
from datetime import date, datetime
from django.views.csrf import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth

today = datetime.now()
today_format = today.strftime("%d-%m-%Y")

# Create your views here.
def index(request):
    return render(request, 'index.html')