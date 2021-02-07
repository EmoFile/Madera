from rest_framework import serializers

from .models import Devis, Plan, Ticket, Gamme, Composant, Module, Piece


# Serialisation des données en JSON

# Administratif

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id_ticket', 'titre', 'description', 'statut', 'traitement')

class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ('id_plan', 'auteur', 'nom', 'lien_pdf')

class DevisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Devis
        fields = ('id_devis', 'prix', 'nom_devis', 'commercial', 'client', 'plan', 'pieces')

# Produits

class GammeSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Gamme
        fields = ('id_gamme', 'nom')

class ComposantSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Composant
        fields = ('id_composant', 'nom' , 'prix')

class ModuleSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Module
        fields = ('id_module', 'nom', 'gamme', 'composants')

class PieceSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Piece
        fields = ('id_piece', 'nom', 'modules')