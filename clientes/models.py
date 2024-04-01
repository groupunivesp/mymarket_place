from django.db import models

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.phone} {self.address} {self.username} {self.password}"
    
    
class Visitante(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.phone} {self.address} {self.username} {self.password}"
    
class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, null=True)
    price = models.CharField(max_length=8, null=True)
    
    def __str__(self):
        return f"{self.id} {self.name} {self.price}"