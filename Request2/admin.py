from django.contrib import admin

# Register your models here.

from Request2.models import requestCla, RequestType

admin.site.register([requestCla, RequestType])