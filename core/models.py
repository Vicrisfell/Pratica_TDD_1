from django.db import models

class LivroModel(models.Model):
    titulo = models.CharField('Título', max_length=200,)
    editora = models.CharField('editora', max_length=200,)
    autor = models.CharField('autor', max_length=200,)
    isbn = models.CharField('isbn', max_length=13,)
    ano = models.CharField('ano', max_length=4,)
    paginas=models.CharField('paginas',max_length=3)

    def __str__(self):
        return self.titulo