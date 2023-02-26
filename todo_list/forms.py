from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=45,label='',
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter todo e.g Grocery shopping',
    'aria-label':'Todo','aria-describeby':'add-btn'}))
