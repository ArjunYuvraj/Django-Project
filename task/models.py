from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField()    
    category = models.CharField(max_length=50, choices=[
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('urgent', 'Urgent'),
        ('other', 'Other'),
    ])
    
    def __str__(self):
        return self.title
