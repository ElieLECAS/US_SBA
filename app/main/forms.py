from django import forms
from .models import PredictApi

class PredictApiForm(forms.ModelForm):
    class Meta:
        model = PredictApi
        fields = "__all__"
        labels = {
            'F1' : 'Entrez la sepal_lenght',
            'F2' : 'Entrez la sepal_width',
            'F3' : 'Entrez la petal_lenght',
            'F4' : 'Entrez la petal_width',
        }