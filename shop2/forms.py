from django import forms

class Form(forms.Form):
    username = forms.Charfield()
    age = forms.Integerfield()
    form = forms