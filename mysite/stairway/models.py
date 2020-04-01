from django.conf import settings
from django.db import models
from django.utils import timezone

class Admin(models.Model):
    admin_name = models.CharField(null=False, max_length=50)
    admin_email = models.EmailField(null=False)
    admin_password = models.CharField(null=False, max_length=20)
    admin_created_date = models.DateTimeField(default=timezone.now)

