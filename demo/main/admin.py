from django.contrib import admin
from .models import customer, rocket, payload, launch, Tenant  # importing the models
from .utils import tenant_from_request
# Register your models here.

class customerAdmin(admin.ModelAdmin):
    exclude = ('tenant',)
    
    def get_queryset(self, request, *args, **kwargs):
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_from_request(request)
        queryset = queryset.filter(tenant=tenant)
        return queryset
    
    def save_model(self, request, obj, form, change):
        tenant = tenant_from_request(request)
        obj.tenant = tenant
        super().save_model(request, obj, form, change)
        

class rocketAdmin(admin.ModelAdmin):
    exclude = ('tenant',)

    
    def get_queryset(self, request, *args, **kwargs):
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_from_request(request)
        queryset = queryset.filter(tenant=tenant)
        return queryset
    
    def save_model(self, request, obj, form, change):
        tenant = tenant_from_request(request)
        obj.tenant = tenant
        super().save_model(request, obj, form, change)
        

class payloadAdmin(admin.ModelAdmin):
    exclude = ('tenant',)

    
    def get_queryset(self, request, *args, **kwargs):
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_from_request(request)
        queryset = queryset.filter(tenant=tenant)
        return queryset
    
    def save_model(self, request, obj, form, change):
        tenant = tenant_from_request(request)
        obj.tenant = tenant
        super().save_model(request, obj, form, change)


class launchAdmin(admin.ModelAdmin):
    exclude = ('tenant',)
    
    
    def get_queryset(self, request, *args, **kwargs):
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_from_request(request)
        queryset = queryset.filter(tenant=tenant)
        return queryset
    
    def save_model(self, request, obj, form, change):
        tenant = tenant_from_request(request)
        obj.tenant = tenant
        super().save_model(request, obj, form, change)
        

admin.site.register(customer, customerAdmin)
admin.site.register(rocket, rocketAdmin)
admin.site.register(payload, payloadAdmin)
admin.site.register(launch, launchAdmin)
admin.site.register(Tenant)