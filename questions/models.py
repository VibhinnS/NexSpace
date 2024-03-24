from django.db import models

class Question(models.Model):
    title:str = models.TextField()
    content:str = models.TextField()
    