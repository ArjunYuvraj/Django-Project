from django.db import models
from datetime import date

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Needs Review', 'Needs Review'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default=" no descrition available")
    due_date = models.DateField(default=date.today)    
    category = models.CharField(max_length=50, choices=[
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('urgent', 'Urgent'),
        ('other', 'Other'),
    ])
    status = models.CharField(max_length=50, choices=STATUS_CHOICES) 
    
    def __str__(self):
        return self.title
