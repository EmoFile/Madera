"""BACK_END URL Configuration

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
from django.urls import path, include
from rest_framework import routers

from API_REST_MADERA import views
from API_REST_MADERA.views import DevisDetailViewSet, PlanDetailViewSet, TicketDetailViewSet

router = routers.DefaultRouter()
router.register(r'tickets', views.PlansViewSet, 'tickets')
router.register(r'plans', views.PlansViewSet, 'plans')
router.register(r'devis', views.DevisViewSet, 'devis')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest-framework'))
]
urlpatterns += [
    path('ticket/<int:pk>', TicketDetailViewSet.as_view(), name="ticket-detail"),
    path('plan/<int:pk>', PlanDetailViewSet.as_view(), name="plan-detail"),
    path('devis/<int:pk>', DevisDetailViewSet.as_view(), name="devis-detail"),
]