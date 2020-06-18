from django.db import models

# Create your models here.
class Interviews(models.Model):
    Embed_Youtube_Code = models.CharField(max_length=150)
    
    
    
    def __str__(self):
        return self.Embed_Youtube_Code
        

