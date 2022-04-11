from django.shortcuts import render
from baseapp.models import *
from django.conf import settings
from django.http import request
from django.shortcuts import render
from django.shortcuts import render, redirect
# Create your views here.


def BootstrapDash(request):
    return render(request,'BootstrapDash.html')