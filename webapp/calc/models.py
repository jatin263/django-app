from django.db import models
# Create your models here.
class users(models.Model):
    id=models.BigIntegerField(primary_key=True,default=0)
    name=models.CharField(max_length=100,default="xxxxx")
    username=models.CharField(max_length=100,default="xxxx")
    password=models.CharField(max_length=100,default="xxxxxx")

    class Meta:
        db_table=""
        managed=True
        verbose_name='User'
        verbose_name_plural='Users'

class students(models.Model):
    id=models.CharField(max_length=200,primary_key=True,default=0)
    name=models.CharField(max_length=200,default="xxxxxx")
    email=models.EmailField(max_length=200,default="xyz@xyz.com")

    class Meta:
        db_table=""
        managed=True
        verbose_name='Student'
        verbose_name_plural='Students'
        
