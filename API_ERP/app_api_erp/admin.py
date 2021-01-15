from django.contrib import admin

# Register your models here.
from app_api_erp.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('firstname',
                    'lastname',
                    'e_mail')
    list_display_links = list_display

admin.site.register(Client, ClientAdmin)
