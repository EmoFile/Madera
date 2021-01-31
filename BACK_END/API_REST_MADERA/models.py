from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Utilisateurs

class UserIT(AbstractBaseUser) :
    nom = models.CharField(max_length=50);
    prenom = models.CharField(max_length=50);

class UserIT(AbstractBaseUser) :
    nom = models.CharField(max_length=50);
    prenom = models.CharField(max_length=50);

class UserAdministration(AbstractBaseUser) :
    nom = models.CharField(max_length=50);
    prenom = models.CharField(max_length=50);

class UserBE(AbstractBaseUser) :
    nom = models.CharField(max_length=50);
    prenom = models.CharField(max_length=50);

class Commercial(AbstractBaseUser) :
    nom = models.CharField(max_length=50);
    prenom = models.CharField(max_length=50);

class Client(AbstractBaseUser) :
    mail = models.CharField(max_length=50);

# Administratif

class Ticket(models.Model) :
    id_ticket = models.AutoField(primary_key=True);
    titre = models.CharField(max_length=50);
    description = models.TextField();
    statut = models.CharField(max_length=25);

    def __str__(self):
        return self.titre

class Plan(models.Model) :
    id_plan = models.AutoField(primary_key=True);
    #user_be = models.ForeignKey(User, on_delete=models.CASCADE);
    nom = models.CharField(max_length=60);
    lien_pdf = models.CharField(max_length=100);

    def __str__(self):
        return self.nom_devis

class Devis(models.Model) :
    id_devis = models.AutoField(primary_key=True);
    #commercial = models.ForeignKey(User, on_delete=models.CASCADE);
    #client = models.ForeignKey(User, on_delete=models.CASCADE);
    prix = models.DecimalField(max_digits=10, decimal_places=2);
    nom_devis = models.CharField(max_length=60);
    #plan = models.ForeignKey(Plan, on_delete=models.CASCADE);

    def __str__(self):
        return self.nom_devis

# Produits

class Piece(models.Model) :
    id_piece = models.AutoField(primary_key=True);
    nom = models.CharField(max_length=50);

    def __str__(self):
        return self.nom

class Gamme(models.Model) :
    id_gamme = models.AutoField(primary_key=True);
    nom = models.CharField(max_length=50);

    def __str__(self):
        return self.nom

class Module(models.Model) :
    id_module = models.AutoField(primary_key=True);
    nom = models.CharField(max_length=50);

    def __str__(self):
        return self.nom

class Composant(models.Model) :
    id_composant = models.AutoField(primary_key=True);
    nom = models.CharField(max_length=50);
    prix = models.DecimalField(max_digits=10, decimal_places=2);

    def __str__(self):
        return self.nom