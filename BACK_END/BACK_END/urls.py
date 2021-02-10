from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from API_REST_MADERA import views
from API_REST_MADERA.views import DevisDetailViewSet, PlanDetailViewSet, TicketDetailViewSet, GammeDetailViewSet, \
    ComposantDetailViewSet, ModuleDetailViewSet, PieceDetailViewSet, ModuleComposantDetailViewSet, products, \
    ManualAPIDevis, DevisListView, ManualAPICreateUserInterne, ManualAPIAccepterDevis, ManualAPIRefuserDevis, \
    ManualAPICreateUser, CompteDetailViewSet, ManualAPIAddPlan, ManualAPIAddPlanTODevis, ManualAPIAuthentication

router = routers.DefaultRouter()

router.register(r'tickets', views.TicketsViewSet, 'tickets')
router.register(r'plans', views.PlansViewSet, 'plans')
router.register(r'devis', views.DevisViewSet, 'devis')

router.register(r'gammes', views.GammeViewSet, 'gammes')
router.register(r'composants', views.ComposantViewSet, 'composants')
router.register(r'modules', views.ModuleViewSet, 'modules')
router.register(r'modulecomposant', views.ModuleComposantViewSet, 'modulecomposant')
router.register(r'pieces', views.PieceViewSet, 'pieces')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest-framework')),
    path('create-internal-user/', ManualAPICreateUserInterne.as_view(), name="create-user-internal-api"),
    path('create-user/', ManualAPICreateUser.as_view(), name="create-user-api"),
    path('compte/<int:pk>', CompteDetailViewSet.as_view(), name="compte-detail"),
    path('products/', products, name='products')
]
urlpatterns += [
    path('ticket/<int:pk>', TicketDetailViewSet.as_view(), name="ticket-detail"),
    path('plan/<int:pk>', PlanDetailViewSet.as_view(), name="plan-detail"),
    path('devis/<int:pk>', DevisDetailViewSet.as_view(), name="devis-detail"),

    path('gamme/<int:pk>', GammeDetailViewSet.as_view(), name="gamme-detail"),
    path('composant/<int:pk>', ComposantDetailViewSet.as_view(), name="composant-detail"),
    path('module/<int:pk>', ModuleDetailViewSet.as_view(), name="module-detail"),
    path('modulecomposant/<int:pk>', ModuleComposantDetailViewSet.as_view(), name="modulecomposant-detail"),
    path('piece/<int:pk>', PieceDetailViewSet.as_view(), name="piece-detail"),
]

urlpatterns += [
    path('create-devis/', ManualAPIDevis.as_view(), name="create-devis-manual-api"),
    path('get-devis/', DevisListView.as_view(), name="list-devis-manual-api"),
    path('accept-devis/', ManualAPIAccepterDevis.as_view(), name="accept-devis-manual-api"),
    path('cancel-devis/', ManualAPIRefuserDevis.as_view(), name="cancel-devis-manual-api"),
    path('send-plan/', ManualAPIAddPlan.as_view(), name="send-plan-manual-api"),
    path('add-plan-to-devis/', ManualAPIAddPlanTODevis.as_view(), name="add-plan-to-devis-manual-api"),
    path('manual-api-auth/login/', ManualAPIAuthentication.as_view(), name="api-auth-login-devis-manual-api"),
]
