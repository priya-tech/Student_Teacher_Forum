from .models import AdduserModel,AddQuestionsModel
from django.forms import ModelForm

class AdduserForm(ModelForm):
    class Meta:
        model=AdduserModel
        fields=['name','email','password','usertype']

class AddQuestionsForm(ModelForm):
    class Meta:
        model=AddQuestionsModel
        fields=['name','title','content','date']
