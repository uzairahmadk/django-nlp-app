from django import forms

class TextProcessingForm(forms.Form):

    text = forms.CharField(label='Input your text here', widget=forms.Textarea(attrs={"class":"form-control", "id":"InputText", "placeholder":"Input your text here"}), required=True)

    class Meta:
        fields = ('text')
