from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=100,null=True)
    age=models.IntegerField(null=True)
    phone_Number=models.BigIntegerField(null=True)
    dept=models.CharField(max_length=100,null=True)
    Email_id=models.CharField(max_length=100,null=True)
    Event_name=models.CharField(max_length=100,null=True)
    tot_members=models.IntegerField(null=True)


    def __str__(self):
        return self.name+"-"+self.dept

   
    

