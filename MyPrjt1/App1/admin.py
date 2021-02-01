from django.contrib import admin
from .models import Client,Company,Bank

# Register your models here.
admin.site.register(Company)
admin.site.register(Client)
admin.site.register(Bank)