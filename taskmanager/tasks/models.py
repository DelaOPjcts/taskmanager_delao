# tasks/models.py

from django.db import models
from django.utils import timezone
from datetime import timedelta  # Importar timedelta desde datetime

def get_due_date():
    return timezone.now().date() + timedelta(days=1)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(default=get_due_date)  # Usar la función
    
    def __str__(self):
        return self.title
