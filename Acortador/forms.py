from django import forms

class AcortarNuevaUrl(forms.Form):
    url=forms.CharField(label='Inserta tu URL')
    