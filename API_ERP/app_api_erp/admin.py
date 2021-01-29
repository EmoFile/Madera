from django.contrib import admin

# Register your models here.
from app_api_erp.models import Client, InternalUser


class ClientAdmin(admin.ModelAdmin):
    list_display = ('firstname',
                    'lastname',
                    'e_mail')
    list_display_links = list_display


class InternalUserAdmin(admin.ModelAdmin):
    list_display = ('firstname',
                    'lastname',
                    'e_mail')
    list_display_links = list_display


admin.site.register(Client, ClientAdmin)
admin.site.register(InternalUser, InternalUserAdmin)
