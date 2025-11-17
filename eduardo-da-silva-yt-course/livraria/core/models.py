from django.db import models
from django.contrib.auth.models import User

# Categoria
class Categoria(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao

# Editora
class Editora(models.Model):
    nome = models.CharField(max_length = 255)
    site = models.URLField()

    def __str__(self):
        return self.nome

# Autor
class Autor(models.Model):
    nome = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.nome
    
    class Meta():
        verbose_name_plural = "autores"
    


class Livro(models.Model):
    nome = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="livros")
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros")
    autor = models.ManyToManyField(Autor, related_name="livros")


    def __str__(self):
        return f"{self.nome} ({self.editora})"

class Compra(models.Model):

    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZADO = 2, "Realizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)