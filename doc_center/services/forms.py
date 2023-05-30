from django import forms

from .models import Service

INPUT_CLASS = "w-full rounded-lg mb-3 mt-3"


class RequestForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = {"name","type", "description", "price"}
        widgets = {
            "name": forms.TextInput(attrs={"class": INPUT_CLASS}),
            "type": forms.Select(attrs={'class': INPUT_CLASS}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASS}), 
            "price": forms.NumberInput(attrs={"class": INPUT_CLASS})
        }