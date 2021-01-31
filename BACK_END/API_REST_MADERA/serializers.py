from rest_framework import serializers

from .models import Devis, Plan

# Serialisation des données en JSON

class DevisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Devis
        fields = ('id_devis', 'prix', 'nom_devis')

class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ('id_plan', 'nom', 'lien_pdf')