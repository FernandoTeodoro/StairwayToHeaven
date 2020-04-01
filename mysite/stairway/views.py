from django.shortcuts import render
from .models import *

def create_admin(request):
    return render(request, "templates/formAdmin.html")


def cadastrar_admin(request):
    form = AdminForm()
    return render(request, "templates/formAdmin.html", {'form':form})
