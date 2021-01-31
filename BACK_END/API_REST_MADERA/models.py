from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Utilisateurs (DOIVENT HERITER DE COMPTE CLIENT QUI EST A VERIFIER SI IL EST STOCKER ICI OU DANS L'ERP)

class UserIT(AbstractBaseUser) :
    nom = models.CharField(max_length=50);
    prenom = models.CharField(max_length=50);

    def __str__(self):
        return self.prenom + " " + self.nom

class UserAdministration(AbstractBaseUser) :
    nom = models.CharField(max_length=50);
    prenom = models.CharField(max_length=50);

    def __str__(self):
        return self.prenom + " " + self.nom

class UserBE(AbstractBaseUser) :
    nom = models.CharField(max_length=50);
    prenom = models.CharField(max_length=50);

    def __str__(self):
        return self.prenom + " " + self.nom

class Commercial(AbstractBaseUser) :
    nom = models.CharField(max_length=50);
    prenom = models.CharField(max_length=50);

    def __str__(self):
        return self.prenom + " " + self.nom

class Client(AbstractBaseUser) :
    mail = models.CharField(max_length=50);

    def __str__(self):
        return self.prenom + " " + self.nom

# Produits

class Gamme(models.Model) :
    id_gamme = models.AutoField(primary_key=True);
    nom = models.CharField(max_length=50);

    def __str__(self):
        return self.nom

class Composant(models.Model) :
    id_composant = models.AutoField(primary_key=True);
    nom = models.CharField(max_length=50);
    prix = models.DecimalField(max_digits=10, decimal_places=2);

    def __str__(self):
        return self.nom

class Module(models.Model) :
    id_module = models.AutoField(primary_key=True);
    nom = models.CharField(max_length=50);
    gamme = models.OneToOneField(Gamme, on_delete=models.CASCADE, null=True, blank=True);
    composants = models.ForeignKey(Composant, on_delete=models.CASCADE, null=True, blank=True);

    def __str__(self):
        return self.nom

class Piece(models.Model) :
    id_piece = models.AutoField(primary_key=True);
    nom = models.CharField(max_length=50);
    modules = models.ForeignKey(Module, on_delete=models.CASCADE, null=True, blank=True);

    def __str__(self):
        return self.nom

# Administratif

class Ticket(models.Model) :
    id_ticket = models.AutoField(primary_key=True);
    titre = models.CharField(max_length=50);
    description = models.TextField();
    statut = models.CharField(max_length=25);
    traitement = models.ForeignKey(UserIT, on_delete=models.CASCADE, null=True, blank=True);
    #demande = models.ForeignKey(UserBE, UserAdministration, Commercial, models.CASCADE);

    def __str__(self):
        return self.titre + self.statut

class Plan(models.Model) :
    id_plan = models.AutoField(primary_key=True);
    auteur = models.OneToOneField(UserBE, on_delete=models.CASCADE, null=True, blank=True);
    nom = models.CharField(max_length=60);
    lien_pdf = models.CharField(max_length=100);

    def __str__(self):
        return self.nom

class Devis(models.Model) :
    id_devis = models.AutoField(primary_key=True);
    prix = models.DecimalField(max_digits=10, decimal_places=2);
    nom_devis = models.CharField(max_length=60);
    commercial = models.OneToOneField(Commercial, on_delete=models.CASCADE, null=True, blank=True);
    client = models.OneToOneField(Client, on_delete=models.CASCADE, null=True, blank=True);
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE, null=True, blank=True);
    pieces = models.ForeignKey(Piece,on_delete=models.CASCADE, null=True, blank=True);

    def __str__(self):
        return self.nom_devis