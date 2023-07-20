from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20,blank=True)
    address = models.TextField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    