from rest_framework import serializers

from .models import Devis, Plan, Ticket


# Serialisation des données en JSON

# Administratif

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id_ticket', 'titre', 'description', 'statut')

class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ('id_plan', 'nom', 'lien_pdf')

class DevisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Devis
        fields = ('id_devis', 'prix', 'nom_devis')

# Produits