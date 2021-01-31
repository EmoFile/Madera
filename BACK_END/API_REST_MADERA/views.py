from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Devis, Plan, Ticket
from .serializers import DevisSerializer, PlanSerializer, TicketSerializer


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
