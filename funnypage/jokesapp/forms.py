from django import forms


class JokeForm(forms.Form):
    user_name = forms.CharField(label="Váše jméno", max_length=100)





