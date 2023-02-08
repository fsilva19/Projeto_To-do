from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(
        label='Título'
    )
    class Meta:
        model = Task
        fields = ['title', 'description']
        
        