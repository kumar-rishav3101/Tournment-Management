from django import forms
from .models import Tournment,Teams,Player

class Tournment(forms.ModelForm):
    class Meta():
        model = Tournment
        fields =('__all__')

class Teams(forms.ModelForm):
    class Meta():
        model = Teams
        fields =('__all__')

class Player(forms.ModelForm):
    class Meta():
        model = Player
        fields =('__all__')
