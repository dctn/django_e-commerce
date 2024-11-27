from django import forms
from .models import *

class SizeChoice(models.TextChoices):
    small = ("sm","Small")
    medium = ("md","Medium")
    large = ("lg","Large")

class AtcForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ("size",)

    size = forms.ChoiceField(required=True,choices=SizeChoice)
    color = forms.ModelChoiceField(required=True,queryset=Colors.objects.all())

    # widgets = {
    #     'colors': forms.model()
    # }