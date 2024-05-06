from django.db import models

from django. contrib. auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):  
    Name=models.CharField(max_length=100,verbose_name="Name")
    Address=models.CharField(max_length=100,verbose_name="Address")
    Phoneno=models.IntegerField(verbose_name="Phone")
    Age=models.IntegerField(verbose_name="age")
    Qualification=models.CharField(max_length=100,verbose_name="Qualification")
    Djoin=models.DateField(verbose_name="Joining Date")
    Status=models.IntegerField(verbose_name="Status", default='0')
    usertype=models.CharField(max_length=20)

    class Meta:  
        db_table = "Usertable" 
