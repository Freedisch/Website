from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)
    image=models.ImageField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name