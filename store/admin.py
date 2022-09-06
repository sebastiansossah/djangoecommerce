from django.contrib import admin

# Register your models here.

from store.models import productModel, productCategory

#creamos los campos de solo lectura 
class adminStore(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_updated')

admin.site.register(productCategory)
admin.site.register(productModel)
