import json

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
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
        modules_json = serializers.serialize("json", modules, fields=('nom', 'gamme'))

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


class ManualAPIPiece(generic.View):
    """
    Only post can be called in this view
    """
    http_method_names = ['post']

    @method_decorator(never_cache)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Only Request with id in his JSON will work. If the ID is not existing in the base tha t will do 404 or 403
        In the production the security will check the IP (like the logg tell)
        :param request: Mandatory: the request with the POST where the ID is mandatory. if id is not existing error 404
        :return HttpResponse:
        """
        try:
            received = json.loads(request.body)
            prix = received["prix"]
            client = received["client"]
            commercial = received["commercial"]
            nom = received["nom_devis"]
            pieces = received["pieces"]
            cpt = 0
            devis = None
            for piece in pieces:
                created_piece = Piece.objects.create(nom=piece["nom"])
                created_piece.save()
                for module in piece["modules"]:
                    created_piece.modules.add(Module.objects.get(id_module=module["id_module"]))
                created_piece.save()
                if cpt == 0:
                    devis = Devis.objects.create(nom_devis=nom, prix=prix, client=client, commercial=commercial)
                    devis.save()
                    devis.pieces.add(created_piece)
                    cpt += 1
                else:
                    devis.pieces.add(created_piece)
                    devis.save()
            return HttpResponse('200')
        except:
            return HttpResponse('400')
