from django.contrib import admin
from .models import customer, rocket, payload, launch, Tenant  # importing the models
# Register your models here.

admin.site.register(customer)
admin.site.register(rocket)
admin.site.register(payload)
admin.site.register(launch)
admin.site.register(Tenant)