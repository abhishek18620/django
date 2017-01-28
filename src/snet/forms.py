from django import forms
form .models import user_info

class registration(forms.Form):
    uname = forms.CharField(max_length=10)  # primary key
    name = forms.CharField(max_length=30)
    password = forms.BooleanField()
    graph_score = forms.IntegerField()
