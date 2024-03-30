from django.contrib import admin
from .models import Cliente, Visitante


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "lastname", "phone", "address")

admin.site.register(Cliente, ClienteAdmin)


class VisitanteAdmin(admin.ModelAdmin):
    list_display = ("id","firstname", "lastname", "phone","address", "username", "password")
    
admin.site.register(Visitante, VisitanteAdmin)

