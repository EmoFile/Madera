from rest_framework import serializers

from .models import Devis, Plan, Ticket, Gamme, Composant, Module, Piece, ModuleComposant


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


class GammeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gamme
        fields = ('id_gamme', 'nom')


class ComposantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Composant
        fields = ('id_composant', 'nom', 'prix')


class ModuleComposantSerializer(serializers.Serializer):
    composant = serializers.IntegerField()
    quantity = serializers.IntegerField()
    # cmpt = ComposantSerializer(many=True)
    # nom = serializers.RelatedField(source='composant', read_only=True)
    #composant = serializers.ManyRelatedField(child_relation='composant', read_only=True)

    class Meta:
        model = ModuleComposant
        fields = ['composant', 'quantity']


class ModuleSerializer(serializers.ModelSerializer):
    composants = ModuleComposantSerializer(many=True)

    class Meta:
        model = Module
        fields = ('id_module', 'nom', 'gamme', 'composants')

    def create(self, validated_data):
        module = Module.objects.create(nom=validated_data['nom'], gamme=validated_data['gamme'])
        module.save()

        for module_composant in validated_data['composants']:
            created = ModuleComposant(composant=module_composant['composant'].id_composant,
                                      quantity=module_composant['quantity'],
                                      module=module.id_module)
            created.save()


class PieceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Piece
        fields = ('id_piece', 'nom', 'modules')
