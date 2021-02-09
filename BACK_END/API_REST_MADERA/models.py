from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


# Utilisateurs

# Gestionnaire Création Utilisateurs
class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        values = [email]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser doit avoir la variable is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser doit avoir la variable is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

# Classe mère Compte dont dépends tous les autres comptes
class Compte(AbstractBaseUser, PermissionsMixin) :
    email = models.EmailField(unique=True)
    departement = models.CharField(max_length=50)
    id_user = models.AutoField(primary_key=True)
    id_erp = models.IntegerField(unique=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']


# Compte pour User IT
class UserIT(Compte) :
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def __str__(self):
        return self.email


# Compte pour User Admnistration
class UserAdministration(Compte) :
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def __str__(self):
        return self.email


# Compte pour User Bureau d'Etudes
class UserBE(Compte) :
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def __str__(self):
        return self.email


# Compte pour Commercial
class Commercial(Compte) :
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def __str__(self):
        return self.email


# Compte pour Client
class Client(Compte) :

    def __str__(self):
        return self.email

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
    demande = models.ForeignKey(Compte, on_delete=models.CASCADE, null=True, blank=True)

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
