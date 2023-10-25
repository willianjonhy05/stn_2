from django.forms import ModelForm
from .models import Nerd

class NerdForm(ModelForm):

    class Meta:
        model=Nerd
        fields='__all__'