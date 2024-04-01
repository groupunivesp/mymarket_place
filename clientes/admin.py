from django.contrib import admin
from .models import Cliente, Visitante, Produto


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "lastname", "phone", "address")

admin.site.register(Cliente, ClienteAdmin)


class VisitanteAdmin(admin.ModelAdmin):
    list_display = ("id","firstname", "lastname", "phone","address", "username", "password")
    
admin.site.register(Visitante, VisitanteAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")
    
admin.site.register(Produto, ProdutoAdmin)