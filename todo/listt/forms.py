from datetime import datetime
from django.forms import DateTimeField, ModelForm
from django import forms

from listt.models import todo
class TODOForm(forms.ModelForm):
    deadline_date = forms.DateTimeField(
        
        widget=forms.widgets.DateInput(attrs={'type':'date'}),
     )
    deadline_time = forms.DateTimeField(
        
          widget=forms.widgets.TimeInput(attrs={'type':'time'})
     )
   
    class Meta:
        model = todo
        fields = ['title' , 'status' , 'priority','deadline_date','deadline_time']
       
        