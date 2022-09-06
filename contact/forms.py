from django import forms

class form(forms.Form):
    name = forms.CharField(label='Name ', max_length=80, required= True)
    email = forms.CharField(label='Email ', max_length=80, required= True)
    content = forms.CharField(label='Your message', max_length=80, widget=forms.Textarea)


