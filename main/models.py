from unicodedata import name
from django.db import models

# Create your models here.

class PostModel(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'