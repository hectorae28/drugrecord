from django.db import models

# Create your models here.
class Drugs(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    profile=models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    name=models.Charfield(max_length=30)
    num_boxs=models.IntegerField()
    num_gelcaps=models.IntegerField()#number of caps
    mg=models.IntegerField()#mg of gelcaps
    dose=models.IntegerField()#dosis/dia