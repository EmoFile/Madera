import json
import sys
import requests

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt

from app_api_erp.models import Client


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
            if isinstance(received['e_mail'], str) and isinstance(received['phone_number'], str) \
                    and isinstance(received['address'], str) and isinstance(received['firstname'], str) \
                    and isinstance(received['lastname'], str):
                Client.objects.create(
                    lastname=received['lastname'],
                    firstname=received['firstname'],
                    e_mail=received['e_mail'],
                    address=received['address'],
                    phone_number=received['phone_number'],
                )
                return HttpResponse(status=200)
        except ValueError:
            e = sys.exc_info()[0]
            print(e)
        return HttpResponse(status=404)


class IsClientExist(generic.View):
    """
        Only get can be called in this view
        """
    http_method_names = ['get']

    @method_decorator(never_cache)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Only Request with id in his JSON will work, else it will do 404.
        :param request: Mandatory: the request with the POST where the id is mandatory. if id is not
        existing error 404
        :return HttpResponse: 200 or 404
        """
        received = json.loads(request.body)
        if not 'id' in received:
            print(f'no id in JSON | IP : {request.META.get("REMOTE_ADDR")}')
            return HttpResponse(status=404)
        try:
            if isinstance(received['id'], int) and get_object_or_404(Client, id=received['id']):
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=404)
        except ValueError:
            e = sys.exc_info()[0]
            print(e)
            return HttpResponse(status=404)


class GetClientById(generic.View):
    """
        Only get can be called in this view
        """
    http_method_names = ['get']

    @method_decorator(never_cache)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
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
