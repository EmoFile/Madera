from django.core import serializers
from django.http import JsonResponse, HttpResponse
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Devis, Plan, Ticket, Gamme, Composant, Module, Piece, ModuleComposant
from .serializers import DevisSerializer, PlanSerializer, TicketSerializer, GammeSerializer, ComposantSerializer, \
    ModuleSerializer, PieceSerializer, ModuleComposantSerializer


# ADMINISTRATIF
# TICKETS

# Vue Liste des tickets en JSON
class TicketsViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

# Vue Détail du ticket en JSON
class TicketDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

# PLANS

# Vue Liste des plans en JSON
class PlansViewSet(ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

# Vue Détail du plan en JSON
class PlanDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

# DEVIS

# Vue Liste des devis en JSON
class DevisViewSet(ModelViewSet):
    queryset = Devis.objects.all()
    serializer_class = DevisSerializer

# Vue Détail du devis en JSON
class DevisDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Devis.objects.all()
    serializer_class = DevisSerializer

# PRODUITS

# GAMME

# Vue Liste des gammes en JSON
class GammeViewSet(ModelViewSet):
    queryset = Gamme.objects.all()
    serializer_class = GammeSerializer

# Vue Détail de la gamme en JSON
class GammeDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Gamme.objects.all()
    serializer_class = GammeSerializer

# COMPOSANT

# Vue Liste des composants en JSON
class ComposantViewSet(ModelViewSet):
    queryset = Composant.objects.all()
    serializer_class = ComposantSerializer

# Vue Détail du composant en JSON
class ComposantDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Composant.objects.all()
    serializer_class = ComposantSerializer

# MODULE

# Vue Liste des modules en JSON
class ModuleViewSet(ModelViewSet):
    queryset = Module.objects.all().order_by('gamme')
    serializer_class = ModuleSerializer

# Vue Détail du module en JSON
class ModuleDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

# MODULE/COMPOSANT

# Vue Liste des association Module/Composant en JSON
class ModuleComposantViewSet(ModelViewSet):
    queryset = ModuleComposant.objects.all()
    serializer_class = ModuleComposantSerializer

# Vue Détail de la gamme en JSON
class ModuleComposantDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = ModuleComposant.objects.all()
    serializer_class = ModuleComposantSerializer

# PIECE

# Vue Liste des pièces en JSON
class PieceViewSet(ModelViewSet):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer

# Vue Détail de la pièce en JSON
class PieceDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer

# Vue des Gammes ainsi que des Modules correspondants aux gammes et leurs prix
def products(request):
    # Récupération des gammes
    gammes = Gamme.objects.all()

    # Création des listes
    gamme_list = []
    products_list = {'products': gamme_list}

    # Récupération des modules par la gamme
    for gamme in gammes:
        module_list = []
        modules = Module.objects.filter(gamme=gamme)
        modules_json = serializers.serialize("json",modules, fields=('nom', 'gamme'))

        # Récupération des composants à travers la table d'association ModuleComposant
        for module in modules:
            prix_module = 0
            module_composants = ModuleComposant.objects.filter(module=module)
            # Récupération du prix de chaque composant et calcul avec la quantité
            for composant in module_composants:
                quantite = ModuleComposant.objects.get(module=module, composant=composant.composant).quantite
                prix_module += composant.composant.prix * quantite
        module_list.append(modules_json)
        module_gamme = {'nom': gamme.nom, 'modules': module_list}
        gamme_list.append(module_gamme)

    return JsonResponse(products_list)