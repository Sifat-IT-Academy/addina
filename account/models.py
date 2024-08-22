from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    birth_date = models.DateField()
    image = models.BigIntegerField()  # or use ImageField for storing image path

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

