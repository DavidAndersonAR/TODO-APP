from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome # Nome exibido quando chamado
    

class TodoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # data
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # data
    category = models.ForeignKey(Category, default='general', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created'] # Ordenando pelo campo criado

    def __str__(self):
        return self.title # Nome exibido quando chamado