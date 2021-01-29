"""API_ERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app_api_erp.views import CreateClient, IsClientExist, GetClientById, CreateInternalUser, GetInternalUserById

urlpatterns = [
    path('admin/', admin.site.urls),
]
# region Client
urlpatterns += [
    path('CreateClient/', CreateClient.as_view(), name='create_client'),
    path('IsClientExist/', IsClientExist.as_view(), name='is_client_exist'),
    path('GetClientById/', GetClientById.as_view(), name='get_client_by_id'),
]
# endregion
# region InternalUser
urlpatterns += [
    path('CreateInternalUser/', CreateInternalUser.as_view(), name='create_internal_user'),
    path('GetInternalUserById/', GetInternalUserById.as_view(), name='get_internal_user_by_id'),
]
# endregion
