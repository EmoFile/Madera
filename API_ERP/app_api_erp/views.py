import json
import sys
import requests

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt

from app_api_erp.models import Client, InternalUser


# region CLient
class CreateClient(generic.View):
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
        Only Request with e_mail in his JSON will work, else it will do 404
        :param request: Mandatory: the request with the POST where the e_mail is mandatory. if e_mail is not
        existing error 404
        :return HttpResponse: 200 or 404
        """
        received = json.loads(request.body)

        if not 'e_mail' in received:
            print(f'no e_mail in JSON | IP : {request.META.get("REMOTE_ADDR")}')
            return HttpResponse(status=404)
        try:
            print('POST to CreateClient')
            if isinstance(received['e_mail'], str) and isinstance(received['phone_number'], str) \
                    and isinstance(received['address'], str) and isinstance(received['firstname'], str) \
                    and isinstance(received['lastname'], str):
                print('GOOD POST')
                client = Client.objects.create(
                    lastname=received['lastname'],
                    firstname=received['firstname'],
                    e_mail=received['e_mail'],
                    address=received['address'],
                    phone_number=received['phone_number'],
                )
                return JsonResponse({"status": 201,
                                     "id": client.id})
            print('BAD POST')
        except ValueError:
            e = sys.exc_info()[0]
            print(e)
        return HttpResponse(status=404)


class IsClientExist(generic.View):
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
        Only Request with id in his JSON will work, else it will do 404.
        :param request: Mandatory: the request with the POST where the id is mandatory. if id is not
        existing error 404
        :return HttpResponse: 200 or 404
        """
        received = json.loads(request.body)
        if not 'e_mail' in received:
            print(f'no e_mail in JSON | IP : {request.META.get("REMOTE_ADDR")}')
            return HttpResponse(status=404)
        try:
            if isinstance(received['e_mail'], str):
                e_mail = received['e_mail']
                client = Client.objects.get(e_mail=e_mail)
                return JsonResponse({'status':200,
                                     'id': client.id})
            else:
                return HttpResponse(status=404)
        except ValueError:
            e = sys.exc_info()[0]
            print(e)
            return HttpResponse(status=404)


class GetClientById(generic.View):
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
        Only Request with id in his JSON will work, else it will do 404.
        :param request: Mandatory: the request with the POST where the id is mandatory. if id is not
        existing error 404
        :return JSONResponse: {'status' : 200, 'client' : clientGetByID} or HttpResponse: 404
        """
        received = json.loads(request.body)
        if not 'id' in received:
            print(f'no id in JSON | IP : {request.META.get("REMOTE_ADDR")}')
            return HttpResponse(status=404)
        http_json_response = {}
        try:
            if isinstance(received['id'], int) and get_object_or_404(Client, id=received['id']):
                current_client = get_object_or_404(Client, id=received['id'])
                http_json_response['status'] = 200
                client = {'id': current_client.id,
                          'firstname': current_client.firstname,
                          'lastname': current_client.lastname,
                          'address': current_client.address,
                          'e_mail': current_client.e_mail,
                          'phone_numer': current_client.phone_number}
                http_json_response['client'] = client
            else:
                return HttpResponse(status=404)
        except ValueError:
            e = sys.exc_info()[0]
            print(e)
        return JsonResponse(http_json_response)


# endregion

# region InternalUser
class CreateInternalUser(generic.View):
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
        Only Request with e_mail in his JSON will work, else it will do 404
        :param request: Mandatory: the request with the POST where the e_mail is mandatory. if e_mail is not
        existing error 404
        :return HttpResponse: 200 or 404
        """
        received = json.loads(request.body)

        if not 'e_mail' in received:
            print(f'no e_mail in JSON | IP : {request.META.get("REMOTE_ADDR")}')
            return HttpResponse(status=404)
        try:
            print('POST to CreateInternalUser')
            if isinstance(received['e_mail'], str) and isinstance(received['firstname'], str) \
                    and isinstance(received['lastname'], str):
                print('GOOD POST')
                InternalUser.objects.create(
                    lastname=received['lastname'],
                    firstname=received['firstname'],
                    department=received['department'],
                    e_mail=received['e_mail'],
                )
                return HttpResponse(status=200)
            print('BAD POST')
        except ValueError:
            e = sys.exc_info()[0]
            print(e)
        return HttpResponse(status=404)


class GetInternalUserById(generic.View):
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
        Only Request with id in his JSON will work, else it will do 404.
        :param request: Mandatory: the request with the POST where the id is mandatory. if id is not
        existing error 404
        :return JSONResponse: {'status' : 200, 'internal_user' : internalUserGetByID} or HttpResponse: 404
        """
        received = json.loads(request.body)
        if not 'id' in received:
            print(f'no id in JSON | IP : {request.META.get("REMOTE_ADDR")}')
            return HttpResponse(status=404)
        http_json_response = {}
        try:
            if isinstance(received['id'], int) and get_object_or_404(InternalUser, id=received['id']):
                current_internal_user = get_object_or_404(InternalUser, id=received['id'])
                http_json_response['status'] = 200
                internal_user = {'id': current_internal_user.id,
                                 'firstname': current_internal_user.firstname,
                                 'lastname': current_internal_user.lastname,
                                 'department': current_internal_user.department,
                                 'e_mail': current_internal_user.e_mail}
                http_json_response['internal_user'] = internal_user
            else:
                return HttpResponse(status=404)
        except ValueError:
            e = sys.exc_info()[0]
            print(e)
        return JsonResponse(http_json_response)

# endregion
