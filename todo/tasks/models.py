from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Task(models.Model):
    
    STATUS = (
        ('doing', 'Fazendo'),
        ('done', 'Feito'),
    )
    
    title = models.CharField(
        max_length=255
    )
    description = models.CharField(
        max_length=9999
    )
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) #Atualiza data e hora automatico quando CRIA o registro no banco
    updated_at = models.DateTimeField(auto_now=True) #atualiza data e hora automatico quando for atualizado/modificado
    
    def __str__(self):
        return self.title