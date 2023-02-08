from django.db import models

# Create your models here.
class Task(models.Model):
    
    STATUS = (
        ('doing', 'Fazendo'),
        ('done', 'Feito'),
    )
    
    title = models.CharField(
        max_length=255
    )
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    
    created_at = models.DateTimeField(auto_now_add=True) #Atualiza data e hora automatico quando CRIA o registro no banco
    updated_at = models.DateTimeField(auto_now=True) #atualiza data e hora automatico quando for atualizado/modificado
    
    def __str__(self):
        return self.title