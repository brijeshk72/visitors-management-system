from django.db import models

# Register models
class Register_user(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    cname = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    ptm = models.CharField(max_length=50)
    profile = models.ImageField(upload_to='pics/')
    signature = models.ImageField(upload_to='pics/')

    def __str__(self):
        return self.fname