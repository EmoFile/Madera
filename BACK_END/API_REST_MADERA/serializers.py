from rest_framework import serializers

from .models import Devis, Plan, Ticket, Gamme, Composant, Module, Piece, ModuleComposant, Compte


# Serialisation des données en JSON

# Compte
class CompteSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Compte
        fields = ('departement',)

# Administratif

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id_ticket', 'titre', 'description', 'statut', 'traitement')


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id_plan', 'auteur', 'nom', 'lien_pdf')


class DevisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devis
        fields = ('id_devis', 'prix', 'etat', 'nom_devis', 'commercial', 'client', 'plan', 'pieces')


# Produits

class GammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamme
        fields = ('id_gamme', 'nom')


class ComposantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Composant
        fields = ('id_composant', 'nom', 'prix')


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('id_module', 'nom', 'gamme', 'composants')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('id_module', 'nom', 'gamme', 'composants', 'prix')


class ModuleComposantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleComposant
        fields = ('quantite', 'module', 'composant')


class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece
        fields = ('id_piece', 'nom', 'modules')
