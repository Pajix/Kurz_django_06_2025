from django import forms


class JokeForm(forms.Form):
    user_name = forms.CharField(label="Váše jméno", max_length=10,
                                error_messages={"required": "Jméno nesmí být prázdné.",
                                                "max_length": "Prosím, vložte kratší jméno."})





