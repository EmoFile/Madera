from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Devis, Plan, Ticket, Gamme, Composant, Module, Piece
from .serializers import DevisSerializer, PlanSerializer, TicketSerializer, GammeSerializer, ComposantSerializer, \
    ModuleSerializer, PieceSerializer


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

# Vue Liste des gammes en JSON
class ComposantViewSet(ModelViewSet):
    queryset = Composant.objects.all()
    serializer_class = ComposantSerializer

# Vue Détail de la gamme en JSON
class ComposantDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Composant.objects.all()
    serializer_class = ComposantSerializer

# MODULE

# Vue Liste des gammes en JSON
class ModuleViewSet(ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

# Vue Détail de la gamme en JSON
class ModuleDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

# PIECE

# Vue Liste des pièces en JSON
class PieceViewSet(ModelViewSet):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer

# Vue Détail de la pièce en JSON
class PieceDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer