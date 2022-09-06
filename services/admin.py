from django.contrib import admin
from services.models import service

# Register your models here.

class adminService(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(service, adminService)

