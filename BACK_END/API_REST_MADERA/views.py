import json
import requests
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Devis, Plan, Ticket, Gamme, Composant, Module, Piece, ModuleComposant, Commercial, \
    UserAdministration, UserIT, UserBE, Client, PieceModule
from .serializers import DevisSerializer, PlanSerializer, TicketSerializer, GammeSerializer, ComposantSerializer, \
    ModuleSerializer, PieceSerializer, ModuleComposantSerializer


# UTILISATEURS

# Création d'utilisateurs internes
class ManualAPICreateUserInterne(generic.View):
    """
    Only post can be called in this view
    """
    http_method_names = ['post']

    @method_decorator(never_cache)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Récupérer les infos du front
        data = json.loads(request.body)
        user_interne = {"id": int(data["id"])}
        response = requests.post("http://localhost:8001/GetInternalUserById/", json=user_interne)
        data_response = json.loads(response.content)
        if data_response['status'] != 200:
            return HttpResponse(status=400)
        department = data_response['internal_user']['department']

        # Création de l'utilisateur correspondant au département
        if department == "IT":
            UserIT.objects.create(email=data_response['internal_user']['e_mail'],
                                         password=data['password'],
                                         prenom=data_response['firstname'],
                                         nom=data_response['lastname'],
                                         id_erp=int(data["id"])
                                         )
        elif department == "Administrator":
            UserAdministration.objects.create(email=data_response['internal_user']['e_mail'],
                                                     password=data['password'],
                                                     prenom=data_response['internal_user']['firstname'],
                                                     nom=data_response['internal_user']['lastname'],
                                                     id_erp=int(data["id"])
                                                     )
        elif department == "BE":
            UserBE.objects.create(email=data_response['internal_user']['e_mail'],
                                         password=data['password'],
                                         prenom=data_response['internal_user']['firstname'],
                                         nom=data_response['internal_user']['lastname'],
                                         id_erp=int(data["id"])
                                         )
        elif department == "Commercial":
            Commercial.objects.create(email=data_response['internal_user']['e_mail'],
                                             password=data['password'],
                                             prenom=data_response['internal_user']['firstname'],
                                             nom=data_response['internal_user']['lastname'],
                                             id_erp=int(data["id"])
                                             )
        return HttpResponse(status=201)


# Création d'utilisateurs clients
class ManualAPICreateUser(generic.View):
    """
    Only post can be called in this view
    """
    http_method_names = ['post']

    @method_decorator(never_cache)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Récupérer les infos du front et créer l'utilisateur dans le back si il existe déjà dans l'ERP sinon le créer également dans l'ERP
        data = json.loads(request.body)
        email = {"e_mail": data["email"]}
        # Si la case à cocher "Le client existe déjà" est cochée
        if data["isClientExist"] == True:
            response = requests.post("http://localhost:8001/IsClientExist/", json=email)
            print(response)
            data_response = json.loads(response.content)
            # Si le cient existe dans la base ERP
            if data_response['status'] == 200:
                email = data['email']
                password = data['password']
                Client.objects.create(email=email, password=password)
                return HttpResponse(status=201)
        else:
            # Création compte dans l'ERP par appel JSON
            user = {"lastname": data["lastname"],
                    "firstname": data["firstname"],
                    "address": data["address"],
                    "e_mail": data["email"],
                    "phone_number": data["phonenumber"]}
            response = requests.post("http://localhost:8001/CreateClient/", json=user)
            response_json = json.loads(response.content)
            # Création compte dans le BACK avec l'id_erp
            email = data['email']
            password = data['password']
            id_erp = response_json['id']
            Client.objects.create(email=email, password=password, id_erp=id_erp)
            return HttpResponse(status=201)
        return HttpResponse(status=400)


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

    # Création de la liste des gammes
    gamme_list = []

    # Récupération des modules par la gamme
    for gamme in gammes:
        module_list = []
        modules = Module.objects.filter(gamme=gamme)
        # Récupération des composants à travers la table d'association ModuleComposant
        for module in modules:
            current_module = {
                'id': module.id_module,
                'nom': module.nom,
                'prix': 0
            }
            module_composants = ModuleComposant.objects.filter(module=module)
            # Récupération du prix de chaque composant et calcul avec la quantité
            for module_composant in module_composants:
                quantite = ModuleComposant.objects.get(module=module, composant=module_composant.composant).quantite
                current_module['prix'] += module_composant.composant.prix * quantite
            module_list.append(current_module)
        module_gamme = {'nom': gamme.nom, 'modules': module_list}
        gamme_list.append(module_gamme)

    products_list = {'products': gamme_list}
    return JsonResponse(products_list)


class ManualAPIDevis(generic.View):
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
                print(piece["modules"])
                created_piece = Piece.objects.create(nom=piece["nom"])
                created_piece.save()
                for module in piece["modules"]:
                    current_module = Module.objects.get(id_module=module["id_module"])
                    PieceModule(piece=created_piece, module=current_module).save()
                    created_piece.save()
                created_piece.save()
                print(created_piece.modules.all())
                if cpt == 0:
                    devis = Devis.objects.create(nom_devis=nom, prix=prix, client=client, commercial=commercial)
                    devis.save()
                    devis.pieces.add(created_piece)
                    cpt += 1
                else:
                    devis.pieces.add(created_piece)
                    devis.save()
            return HttpResponse('200')
        except Exception:
            raise Exception


class DevisListView(ListView):
    model = Devis

    def get_context_data(self, *args, **kwargs):
        return Devis.objects.all()

    @method_decorator(never_cache)
    @method_decorator(csrf_exempt)
    def get(self, *args, **kwargs):
        devis = self.get_context_data()
        json_devis = []
        try:
            for devi in devis:
                print(f'id_devis: {devi.id_devis}')

                json_devi = {"id_devis": devi.id_devis,
                             "prix": devi.prix,
                             "etat": devi.etat,
                             "nom_devis": devi.nom_devis,
                             "commercial": devi.commercial,
                             "client": devi.client,
                             "plan": devi.plan,
                             "pieces": []}
                pieces = devi.pieces.all()
                for piece in pieces:
                    json_piece = {
                        "id_piece": piece.id_piece,
                        "nom": piece.nom,
                        "prix": 0
                    }
                    json_devi["pieces"].append(json_piece)
                    print(f'id_piece: {piece.id_piece}')
                    print(f'piece.module.count: {piece.modules.count()}')
                    modules = piece.modules.all()
                    print(modules)

                    current_piece_prix = 0
                    for module in modules:
                        module_composants = ModuleComposant.objects.filter(module=module)
                        for module_composant in module_composants:
                            quantite = ModuleComposant.objects.get(module=module,
                                                                   composant=module_composant.composant).quantite
                            current_piece_prix += module_composant.composant.prix * quantite
                    json_piece["prix"] += current_piece_prix
                json_devis.append(json_devi)
            json_response = {"devis": json_devis}
            return JsonResponse(json_response, safe=False)
        except Exception:
            raise Exception


class ManualAPIAccepterDevis(generic.View):
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
            id = received["id"]
            devis = Devis.objects.get(id_devis=id)
            print(devis.etat)
            devis.etat = 'Accepté'
            devis.save()
            print(devis.etat)
            return HttpResponse(200)
        except Exception:
            raise Exception


class ManualAPIRefuserDevis(generic.View):
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
            id = received["id"]
            devis = Devis.objects.get(id_devis=id)
            print(devis.etat)
            devis.etat = 'Refusé'
            devis.save()
            print(devis.etat)
            return HttpResponse(200)
        except Exception:
            raise Exception
