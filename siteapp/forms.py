from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(max_length=120)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
