from django.db import models

# Create your models here.
class Nerd(models.Model):
    nome = models.CharField(max_length=100, default='Nome do Personagem')
    midia = models.CharField(max_length=100, default='Qual o filme/serie/livro')
    profissao = models.CharField(max_length=100, default='Profissão do Personagem')
    sobre = models.TextField(max_length=700, default='Resumo do Filme')
    foto = models.ImageField(upload_to='avatar', default='default_capa.jpg')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Nerd"
        verbose_name_plural = "Nerds"