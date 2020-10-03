from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Drugs(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    profile=models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    name=models.CharField(max_length=30)
    num_boxs=models.IntegerField()
    count_gelcaps_of_box=models.IntegerField()
    num_gelcaps=models.IntegerField()#number of caps
    mg=models.IntegerField()#mg of gelcaps
    dose=models.IntegerField()#dosis/dia