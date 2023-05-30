from django import forms

from .models import Document

INPUT_CLASS = "w-full rounded-lg mb-3 mt-3"

class NewDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = {"name", "categories", "description", "image" }
        widgets = {
            "name": forms.TextInput(attrs={"class": INPUT_CLASS}),
            "categories": forms.Select(attrs={'class': INPUT_CLASS}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASS}), 
            "image": forms.FileInput(attrs={"class": INPUT_CLASS}),
        }


# lend document to a user
class LendDocument(forms.ModelForm):
    class Meta:
        model = Document
        exclude = {"name", "categories", "description", "image", "created_by", "returned", "borrowed", "return_date", "issued_by"}
        widgets = {
            "issued_to": forms.TextInput(attrs={"class": INPUT_CLASS}),
            "return_date": forms.DateInput(attrs={"class": INPUT_CLASS})
        }