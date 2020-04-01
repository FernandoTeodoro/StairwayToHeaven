from django import forms
from .models import *

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ["admin_name", "admin_email", "admin_password", "admin_created_date"]