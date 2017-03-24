from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User, null=False)
    type = models.IntegerField(default=0)
    choice = models.IntegerField(default=-1)
    donation_via_transaction = models.IntegerField(default=0)
    remember_token = models.CharField(blank=True,null=True,max_length=200)
    choice_filled_at=models.DateTimeField()

class Option(models.Model):
    name= models.CharField(max_length=200)
    img_path= models.CharField(blank=True,null=True,max_length=200)
    description= models.CharField(blank=True,null=True,max_length=200)
    price = models.IntegerField(default=0)
    count= models.IntegerField(default=0)
    updated_at= models.DateTimeField()


class Transaction(models.Model):
    id_of_donater= models.IntegerField(default=0)
    webmail_of_donater= models.CharField(max_length=200)
    transactionid= models.IntegerField()
    created_at= models.DateTimeField()
