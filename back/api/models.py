from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import os, uuid


def path_capa(_, filename):
    ext = os.path.splitext(filename)
    return f"capas/{uuid.uuid4().hex}{ext}"


class Autor(models.Model):
    autor = models.CharField(max_length=100)
    s_autor = models.CharField(max_length=100) 
    nasc = models.DateField(null=True, blank=True)
    nacio = models.CharField(max_length=50, null=True, blank=True)
    biogr = models.TextField()
    
    def __str__(self):
        return f'{self.autor} {self.s_autor}'
    

class Editora(models.Model):
    editora = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True, null=True, blank=True)    
    endereco = models.CharField(max_length=200, null=True, blank=True) 
    telefone = models.CharField(max_length=20, null=True, blank=True) 
    email = models.EmailField(null=True, blank=True) 
    site = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.editora
    
    
class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=255)
    descricao = models.TextField()
    idioma = models.CharField(max_length=100, default="Português")
    ano = models.IntegerField(validators=[MinValueValidator(1111), MaxValueValidator(9999)])
    paginas = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    desconto = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    dimensoes = models.CharField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    capa = models.ImageField(upload_to=path_capa, blank=True, null=True)


class Imagem(models.Model):
    Imagem = models.ImageField(upload_to="capas")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Imagem #{self.pk}"
    