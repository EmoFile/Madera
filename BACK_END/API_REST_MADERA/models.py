from django.db import models

# Create your models here.

class Devis(models.Model) :
    id_devis = models.AutoField(primary_key=True);
    prix = models.DecimalField(max_digits=10, decimal_places=2);
    nom_devis = models.CharField(max_length=60);

    def __str__(self):
        return self.nom_devis

class Plan(models.Model) :
    id_plan = models.AutoField(primary_key=True);
    nom = models.CharField(max_length=60);
    lien_pdf = models.CharField(max_length=100);

    def __str__(self):
        return self.nom_devis