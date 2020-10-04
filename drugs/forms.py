from django import forms
from drugs.models import Drugs

class AddForm(forms.ModelForm):
    """user=models.ForeignKey(User, on_delete=models.CASCADE)
    profile=models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    name=forms.CharField(max_length=30)
    num_boxs=forms.IntegerField()
    #count_gelcaps_of_box=forms.IntegerField()
    num_gelcaps=forms.IntegerField()#number of caps
    mg=forms.IntegerField()#mg of gelcaps
    dose=forms.IntegerField()#dosis/dia"""

    class Meta:
        model=Drugs
        fields=('name','num_boxs','num_gelcaps','mg','dose')