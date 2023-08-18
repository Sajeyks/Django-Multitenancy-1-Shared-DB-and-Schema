from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Tenant
from django.conf import settings


@receiver(post_save, sender=Tenant)
def add_tenant_to_hosts(sender, instance, created, **kwargs):
    if created or instance.subdomain_prefix == '':
        
        main_host = 'localhost'
        updated_hostname = f"{instance.subdomain_prefix}.{main_host}"
        
        # Update ALLOWED_HOSTS setting in settings.py
        settings.ALLOWED_HOSTS.append(f"{updated_hostname}")
        

@receiver(pre_delete, sender=Tenant)
def delete_tenant_from_hosts(sender, instance, **kwargs):
    if instance.subdomain_prefix == '':
        
        main_host = 'localhost'
        updated_hostname = f"{instance.subdomain_prefix}.{main_host}"
        
        # Update ALLOWED_HOSTS setting in settings.py
        settings.ALLOWED_HOSTS.remove(f"{updated_hostname}")