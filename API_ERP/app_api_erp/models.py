from django.db import models


# region Client
class Client(models.Model):
    # Nom
    lastname = models.CharField(max_length=25)
    # Prénom
    firstname = models.CharField(max_length=25)
    # Adresse
    address = models.TextField(max_length=250)
    # Adresse mail
    e_mail = models.CharField(max_length=50)
    # Numéro de téléhpone
    phone_number = models.CharField(max_length=10)


# endregion


# region InternalUser
class InternalUser(models.Model):
    BE = 'BE'
    COMMERCIAL = 'Commercial'
    ADMIN = 'Administrator'
    DPT_CHOICES = [
        (BE, 'BE'),
        (COMMERCIAL, 'Commercial'),
        (ADMIN, 'Administrator'),
    ]
    # Nom
    lastname = models.CharField(max_length=25)
    # Prénom
    firstname = models.CharField(max_length=25)
    # Adresse mail
    e_mail = models.CharField(max_length=50)
    # Département
    department = models.CharField(max_length=25,
                                  choices=DPT_CHOICES,
                                  default=COMMERCIAL
                                  )
# endregion
