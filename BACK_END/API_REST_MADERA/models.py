from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


# Utilisateurs

class AccountManager(BaseUserManager):
    def create_user(self, id_erp, password=None):
        if not id_erp:
            raise ValueError("L'utilisateur nécessite un ID ERP")

        user = self.model()
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id_erp, password=None):
        user = self.create_user(id_erp, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class CompteClient(AbstractBaseUser):
    id_user = models.AutoField(primary_key=True)
    id_erp = models.IntegerField(unique=True)
    encrypted_password = models.CharField(max_length=60)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'id_erp'

    def __str__(self):
        return self.id_erp

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class UserIT(CompteClient):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def __str__(self):
        return self.prenom + " " + self.nom


class UserAdministration(CompteClient):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def __str__(self):
        return self.prenom + " " + self.nom


class UserBE(CompteClient):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def __str__(self):
        return self.prenom + " " + self.nom


class Commercial(CompteClient):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def __str__(self):
        return self.prenom + " " + self.nom


class Client(CompteClient):
    mail = models.CharField(max_length=50)

    def __str__(self):
        return self.prenom + " " + self.nom


# Produits

class Gamme(models.Model):
    id_gamme = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Composant(models.Model):
    id_composant = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom


class Module(models.Model):
    id_module = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    gamme = models.ForeignKey(Gamme, on_delete=models.CASCADE, null=True, blank=True)
    composants = models.ManyToManyField(Composant, through="ModuleComposant")

    def __str__(self):
        return self.nom


class ModuleComposant(models.Model):
    quantite = models.IntegerField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True)
    composant = models.ForeignKey(Composant, on_delete=models.CASCADE, null=True)


class Piece(models.Model):
    id_piece = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    modules = models.ManyToManyField('Module', through='PieceModule')

    def __str__(self):
        return self.nom


class PieceModule(models.Model):
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE, null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True)


# Administratif

class Ticket(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=50)
    description = models.TextField()
    statut = models.CharField(max_length=25)
    traitement = models.OneToOneField(UserIT, on_delete=models.CASCADE, null=True, blank=True)
    demande = models.ForeignKey(CompteClient, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titre + self.statut


class Plan(models.Model):
    id_plan = models.AutoField(primary_key=True)
    auteur = models.OneToOneField(UserBE, on_delete=models.CASCADE, null=True, blank=True)
    nom = models.CharField(max_length=60)
    lien_pdf = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Devis(models.Model):
    ENATTENTE = 'En attente'
    ACCEPTE = 'Accepté'
    REFUSE = 'Refusé'
    STATE_CHOICES = [
        (ENATTENTE, 'Enattente'),
        (ACCEPTE, 'Accepte'),
        (REFUSE, 'Refuse'),
    ]
    etat = models.CharField(max_length=20,
                            choices=STATE_CHOICES,
                            default=ENATTENTE)
    id_devis = models.AutoField(primary_key=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    nom_devis = models.CharField(max_length=60)
    commercial = models.OneToOneField(Commercial, on_delete=models.CASCADE, null=True, blank=True)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, null=True, blank=True)
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE, null=True, blank=True)
    pieces = models.ManyToManyField(Piece)

    def __str__(self):
        return self.nom_devis
