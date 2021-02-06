from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from API_REST_MADERA import views
from API_REST_MADERA.views import DevisDetailViewSet, PlanDetailViewSet, TicketDetailViewSet, GammeDetailViewSet, \
    ComposantDetailViewSet, ModuleDetailViewSet, PieceDetailViewSet

router = routers.DefaultRouter()

router.register(r'tickets', views.TicketsViewSet, 'tickets')
router.register(r'plans', views.PlansViewSet, 'plans')
router.register(r'devis', views.DevisViewSet, 'devis')

router.register(r'gammes', views.GammeViewSet, 'devis')
router.register(r'composants', views.ComposantViewSet, 'composants')
router.register(r'modules', views.ModuleViewSet, 'modules')
router.register(r'pieces', views.PieceViewSet, 'pieces')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest-framework'))
]
urlpatterns += [
    path('ticket/<int:pk>', TicketDetailViewSet.as_view(), name="ticket-detail"),
    path('plan/<int:pk>', PlanDetailViewSet.as_view(), name="plan-detail"),
    path('devis/<int:pk>', DevisDetailViewSet.as_view(), name="devis-detail"),

    path('gamme/<int:pk>', GammeDetailViewSet.as_view(), name="gamme-detail"),
    path('composant/<int:pk>', ComposantDetailViewSet.as_view(), name="composant-detail"),
    path('module/<int:pk>', ModuleDetailViewSet.as_view(), name="module-detail"),
    path('piece/<int:pk>', PieceDetailViewSet.as_view(), name="piece-detail"),
]