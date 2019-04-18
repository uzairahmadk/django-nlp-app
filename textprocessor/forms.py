from django import forms
from textprocessor.choices import *

class TextProcessingForm(forms.Form):

    feature_choice = forms.MultipleChoiceField(label='Select your choices', widget=forms.CheckboxSelectMultiple(attrs={"class":"form-check-input", "id": "InputFeature"}), choices=OPTIONS)
    text = forms.CharField(label='Input your text here', widget=forms.Textarea(attrs={"class":"form-control", "id":"InputText", "placeholder":"Input your text here"}), required=True)

    class Meta:
        fields = ('feature_choice', 'text')
