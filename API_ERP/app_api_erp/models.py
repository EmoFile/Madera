from django.db import models

# Create your models here.
class Client:
    #Nom
    lastname = models.CharField(max_length=25)
    #Prénom
    firstname = models.CharField(max_length=25)
    #Adresse
    address = models.TextField(max_length=250)
    #Adresse mail
    e_mail = models.CharField(max_length=50)
