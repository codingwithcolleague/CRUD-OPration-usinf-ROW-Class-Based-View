from django.forms import fields
from ticket.models import Metro
from django  import forms


STATUS_CHOICES = (
    ('inprocess','In Process'),
    ('completed', 'Completed'),
    ('notstarted', 'Not Started')
)

class MetroForm(forms.Form):
    name = forms.CharField(max_length=200)
    mobile = forms.CharField(max_length=200 )
    startplace = forms.CharField(max_length=200 )
    endplace = forms.CharField(max_length=200 )
    status = forms.ChoiceField( choices=STATUS_CHOICES)


class MetroModelForm(forms.ModelForm):
    class Meta:
        model = Metro
        fields= '__all__'