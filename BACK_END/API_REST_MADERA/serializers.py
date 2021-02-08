from rest_framework import serializers

from .models import Devis, Plan, Ticket, Gamme, Composant, Module, Piece, ModuleComposant


# Serialisation des données en JSON

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
        fields = ('id_devis', 'prix', 'nom_devis', 'commercial', 'client', 'plan', 'pieces')

    def create(self, request):
        if request.method == 'POST':
            json_data = request.body
            prix = json_data["prix"]
            client = json_data["client"]
            commercial = json_data["commercial"]
            nom = json_data["commercial"]
            pieces = json_data["pieces"]
            cpt = 0
            devis = None
            for piece in pieces:
                piece = Piece.objects.create(nom=piece.nom)
                piece.save()
                for module in piece["modules"]:
                    piece.modules += Module.objects.get(id_module=module.id_module)
                piece.save()
                if cpt == 0:
                    devis = Devis.objects.create(nom_devis=nom, prix=prix, client=client, commercial=commercial,
                                                 pieces=piece)
                    cpt += 1
                else:
                    devis.pieces += piece
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


