from django.db import models


class RealizadorModel(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    data_de_nascimento = models.DateField(null=False, blank=False)
    sexo = models.CharField(max_length=1, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    funcao = models.CharField(max_length=30, null=False, blank=False)
    foto = models.ImageField(null=True, blank=True)
