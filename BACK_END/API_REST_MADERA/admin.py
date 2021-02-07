from django.contrib import admin
from API_REST_MADERA.models import Devis, UserIT, UserAdministration, UserBE, Commercial, Client, Ticket, Plan, Piece, \
    Gamme, Composant, Module, CompteClient

# Utilisateurs
admin.site.register(CompteClient)
admin.site.register(UserIT)
admin.site.register(UserAdministration)
admin.site.register(UserBE)
admin.site.register(Commercial)
admin.site.register(Client)

# Administratif
admin.site.register(Ticket);
admin.site.register(Plan);
admin.site.register(Devis);

# Produits
admin.site.register(Piece);
admin.site.register(Gamme);
admin.site.register(Composant);
admin.site.register(Module);