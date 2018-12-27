from django import forms

class FormName(forms.Form):
    User_Name = forms.CharField()
    Email = forms.EmailField()
    Text = forms.CharField(widget=forms.Textarea)