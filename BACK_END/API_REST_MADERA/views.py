import json
from datetime import date

import requests
from django.core.files import storage
from django.core.files.storage import default_storage
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from BACK_END import settings
from .models import Devis, Plan, Ticket, Gamme, Composant, Module, Piece, ModuleComposant, Commercial, \
    UserAdministration, UserIT, UserBE, Client, PieceModule, Compte
from .serializers import DevisSerializer, PlanSerializer, TicketSerializer, GammeSerializer, ComposantSerializer, \
    ModuleSerializer, PieceSerializer, ModuleComposantSerializer, CompteSerializer


# UTILISATEURS

# Vue Détail du compte (DEPARTEMENT) en JSON pour filtrage
class CompteDetailViewSet(RetrieveAPIView):
    queryset = Compte.objects.all()
    serializer_class = CompteSerializer


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
                                  prenom=data_response['internal_user']['firstname'],
                                  nom=data_response['internal_user']['lastname'],
                                  id_erp=int(data["id"]),
                                  departement=department
                                  )
        elif department == "Administrator":
            UserAdministration.objects.create(email=data_response['internal_user']['e_mail'],
                                              password=data['password'],
                                              prenom=data_response['internal_user']['firstname'],
                                              nom=data_response['internal_user']['lastname'],
                                              id_erp=int(data["id"]),
                                              departement=department
                                              )
        elif department == "BE":
            UserBE.objects.create(email=data_response['internal_user']['e_mail'],
                                  password=data['password'],
                                  prenom=data_response['internal_user']['firstname'],
                                  nom=data_response['internal_user']['lastname'],
                                  id_erp=int(data["id"]),
                                  departement=department
                                  )
        elif department == "Commercial":
            Commercial.objects.create(email=data_response['internal_user']['e_mail'],
                                      password=data['password'],
                                      prenom=data_response['internal_user']['firstname'],
                                      nom=data_response['internal_user']['lastname'],
                                      id_erp=int(data["id"]),
                                      departement=department
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
                Client.objects.create(email=email, password=password, departement="Client")
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
            Client.objects.create(email=email, password=password, id_erp=id_erp, departement="Client")
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
            client = Client.objects.get(id_user=int(received["client"]))
            commercial = Commercial.objects.get(id_erp=int(received["commercial"]))
            nom = received["nom_devis"]
            pieces = received["pieces"]
            cpt = 0
            devis = None
            for piece in pieces:
                created_piece = Piece.objects.create(nom=piece["nom"])
                created_piece.save()
                for module in piece["modules"]:
                    current_module = Module.objects.get(id_module=module["id_module"])
                    PieceModule(piece=created_piece, module=current_module).save()
                    created_piece.save()
                created_piece.save()
                if cpt == 0:
                    devis = Devis.objects.create(nom_devis=nom, prix=prix, client=client, commercial=commercial)
                    devis.save()
                    devis.pieces.add(created_piece)
                    cpt += 1
                else:
                    devis.pieces.add(created_piece)
                    devis.save()
            Workflow(1)
            return HttpResponse('200')
        except Exception:
            raise Exception


class GetAllClient(ListView):
    model = Client

    def get_context_data(self, *, object_list=None, **kwargs):
        return Client.objects.all()

    @method_decorator(never_cache)
    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        clients = self.get_context_data()
        list_client = []
        try:
            for client in clients:
                json_client = {
                    "id_erp": client.id_erp,
                    "id_client": client.id_user,
                    "mail": client.email,

                }
                list_client.append(json_client)
            json_response = {"clients": list_client}
            return JsonResponse(json_response, safe=False)
        except Exception:
            raise Exception


class DevisListView(generic.View):
    model = Devis

    @method_decorator(never_cache)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        user = Token.objects.get(key=kwargs["token"])
        if ('Client' == user.user.departement):
            client = Client.objects.get(id_user=user.user.id_user)
            return Devis.objects.filter(client=client)
        elif ('Commercial' == user.user.departement):
            commercial = Commercial.objects.get(id_user=user.user.id_user)
            return Devis.objects.filter(commercial=commercial)
        else:
            return Devis.objects.all()

    def post(self, request, *args, **kwargs):
        token = json.loads(request.body)
        devis = self.get_context_data(token=token["token"])

        json_devis = []
        try:
            for devi in devis:
                json_devi = {"id_devis": devi.id_devis,
                             "prix": devi.prix,
                             "etat": devi.etat,
                             "nom_devis": devi.nom_devis,
                             "commercial": devi.commercial.id_user if devi.commercial else None,
                             "client": devi.client.id_user if devi.client else None,
                             "plan": devi.plan.id_plan if devi.plan else None,
                             "pieces": []}
                pieces = devi.pieces.all()
                for piece in pieces:
                    json_piece = {
                        "id_piece": piece.id_piece,
                        "nom": piece.nom,
                        "prix": 0
                    }
                    json_devi["pieces"].append(json_piece)
                    modules = piece.modules.all()

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
            devis.etat = 'Accepté'
            devis.save()
            Workflow(2)
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
            devis.etat = 'Refusé'
            devis.save()
            return HttpResponse(200)
        except Exception:
            raise Exception


def Workflow(workflow_state):
    if workflow_state == 1:
        '''send_mail(
            'Votre devis à été créé',
            'Retrouver sur votre espace client le devis créé afin de le valider',
            'richard.sivera@free.fr',
            ['richard.sivera@free.fr'],
            fail_silently=False,
        )'''
        print('Dire client que sont devis a été établie')
    elif workflow_state == 2:
        print('Dire Service BE que sont devis a été accepté')
    elif workflow_state == 3:
        print('Dire Service Production que les plans ont été ajouté au devis')
        print('Dire Service Achats que les plans ont été ajouté au devis')


class ManualAPIAddPlan(generic.View):
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

        file = request.FILES['file.pdf']

        today = date.today()

        date_time_string = today.strftime("%Y%m%d")
        file_path = './Media/' + date_time_string + '_' + file.name
        file_name = default_storage.save(file_path, file)
        plan = Plan.objects.create(nom=file.name, lien_pdf=file_path)
        id_plan = plan.id_plan
        json_response = {"status": 200, "id_plan": id_plan}
        print(json_response)
        Workflow(3)
        return JsonResponse(json_response)


class ManualAPIAddPlanTODevis(generic.View):
    """
    Only post can be called in this view
    """
    http_method_names = ['post']

    @method_decorator(never_cache)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        print(data)
        id_plan = data["id_plan"]
        id_devis = data["id_devis"]

        print(id_plan)
        print(id_devis)

        devis = Devis.objects.get(id_devis=id_devis)
        plan = Plan.objects.get(id_plan=id_plan)
        devis.plan = plan
        devis.save()

        print(devis.plan)
        return HttpResponse(200)


class ManualAPIAuthentication(generic.View):
    @method_decorator(never_cache)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        email = data["email"]
        if not email:
            return None
        try:
            user = Compte.objects.get(email=email)
        except Compte.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        if user.password != data["password"]:
            return HttpResponse(status=404)
        else:
            token = Token.objects.get_or_create(user=user)
            print(token[0].key)
            user = CompteSerializer(user)
            json_response = {"status": 200,
                             "user": {"id_erp": user.data["id_erp"],
                                      "departement": user.data["departement"],
                                      "token": token[0].key}}
            return JsonResponse(json_response)
