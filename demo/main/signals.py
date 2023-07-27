from django.db.models.signals import post_save, pre_delete, post_migrate
from django.dispatch import receiver
from .models import Tenant
import subprocess
from django.conf import settings


@receiver(post_migrate)
def create_default_tenant(sender, **kwargs):
    # Create the default 'main' tenant on startup if it doesn't exist
    default_tenant, _ = Tenant.objects.get_or_create(name='main', subdomain_prefix='')
    default_tenant.save()

    vm_url_without_https = '{{EDUCATIVE_LIVE_VM_URL}}'.replace('https://', '')
    updated_hostname = f"main.{vm_url_without_https}"
    
    # Update /etc/hosts to replace 'localhost' with 'main'
    update_host_command = f"sudo sed -i '/^127.0.0.1/s/$/ {updated_hostname}/' /etc/hosts"
    subprocess.run(update_host_command, shell=True)

    # Update ALLOWED_HOSTS setting in settings.py
    settings.ALLOWED_HOSTS.append(f"{updated_hostname}")

@receiver(post_save, sender=Tenant)
def add_tenant_to_hosts(sender, instance, created, **kwargs):
    if created or instance.subdomain_prefix == '':
        
        vm_url_without_https = '{{EDUCATIVE_LIVE_VM_URL}}'.replace('https://', '')
        updated_hostname = f"{instance.subdomain_prefix}.main.{vm_url_without_https}"
        
        # Update /etc/hosts to add the new tenant's domain or subdomain
        add_command = f"echo '127.0.0.1 {updated_hostname}' | sudo tee -a /etc/hosts"
        subprocess.run(add_command, shell=True)

        # Update ALLOWED_HOSTS setting in settings.py
        settings.ALLOWED_HOSTS.append(f"{updated_hostname}")


@receiver(pre_delete, sender=Tenant)
def delete_tenant_from_hosts(sender, instance, **kwargs):
    if instance.subdomain_prefix == '':
        
        vm_url_without_https = '{{EDUCATIVE_LIVE_VM_URL}}'.replace('https://', '')
        updated_hostname = f"{instance.subdomain_prefix}.main.{vm_url_without_https}"
        
        # Update /etc/hosts to delete the tenant's domain or subdomain
        delete_command = f"sudo sed -i '/{updated_hostname}/d' /etc/hosts"
        subprocess.run(delete_command, shell=True)

        # Update ALLOWED_HOSTS setting in settings.py
        settings.ALLOWED_HOSTS.remove(f"{updated_hostname}")

