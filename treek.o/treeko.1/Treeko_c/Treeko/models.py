from django.db import models


class proof(models.Model):
    urname = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='pics3')
    image3 = models.ImageField(upload_to='pics3')
    image2 = models.ImageField(upload_to='pics3')
    image4 = models.ImageField(upload_to='pics3')
class newreq(models.Model):
    nickname= models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    area= models.IntegerField(default=2)
    aadhar = models.ImageField(upload_to='pics2')
    land_docs = models.ImageField(upload_to='pics2')