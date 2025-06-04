from django import forms


class JokeForm(forms.Form):
    user_name = forms.CharField(label="Váše jméno",
                                max_length=10,
                                error_messages={"required": "Jméno nesmí být prázdné.",
                                                "max_length": "Prosím, vložte kratší jméno."},
                                widget=forms.TextInput(attrs={"placeholder": "Jméno"})
                                )

    joke_text = forms.CharField(label="Váš vtip",
                                widget=forms.Textarea(attrs={"placeholder": "Vtip"}),
                                max_length=250
                                )

    rating = forms.IntegerField(label="Váš rating",
                                widget=forms.NumberInput(attrs={"placeholder": "Rating"}),
                                min_value=1,
                                max_value=5,
                                )





