from django.contrib import admin
from blog.models import categories, post
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class postAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(categories, categoryAdmin)
admin.site.register(post, postAdmin)