from django.db import models

# Create your models here.

class Person(models.Model):
  Medal_type = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
  name = models.CharField(max_length=30)
  image = models.ImageField(upload_to='myapp1/')
  address = models.CharField(max_length=40)
  email = models.EmailField(max_length=50)
  password = models.CharField(max_length=40)
  medal = models.CharField(blank=True, choices=Medal_type, max_length=10)
  
def __str__(self):
  return self.name