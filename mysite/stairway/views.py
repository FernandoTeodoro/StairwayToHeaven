from django.shortcuts import render
from .models import *
from .forms import AdminForm

def create_admin(request):
    form = AdminForm()
    return render(request, "stairway/formAdmin.html",{'form':form})


def cadastrar_admin(request):
    form = AdminForm()
    return render(request, "stairway/formAdmin.html", {'form':form})
