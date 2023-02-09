from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(
        label='Título'
    )
    description = forms.CharField(
        label='Descrição',
        widget=forms.Textarea,
    )
    class Meta:
        model = Task
        fields = ['title', 'description']
        
        