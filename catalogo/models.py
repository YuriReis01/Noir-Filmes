from django.db import models

# Create your models here.
from django.db import models

class Filme(models.Model):
    GENEROS = [
        ('AÇÃO', 'Ação'),
        ('COMÉDIA', 'Comédia'),
        ('DRAMA', 'Drama'),
        ('TERROR', 'Terror'),
        ('ROMANCE', 'Romance'),
        ('FICÇÃO', 'Ficção Científica'),
        ('ANIMAÇÃO', 'Animação'),
        # adicione mais gêneros se quiser
    ]

    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=20, choices=GENEROS)
    mes_assistido = models.CharField(max_length=20)
    cartaz_url = models.URLField(max_length=300, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.mes_assistido})"


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    mes_assistido = models.CharField(max_length=20)
    poster_url = models.URLField(blank=True, null=True)  # novo campo

    def __str__(self):
        return self.titulo
