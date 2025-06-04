from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import JokeForm  # import z forms.py který jsme si vytvorili a je tam template pro formular
from .models import Jokes


# Create your views here.
def jokes(request):
    # podmínka pokud se odešle formulář, tak se zobrazi stranka s dekujem
    if request.method == "POST":
        form = JokeForm(request.POST)
        if form.is_valid():
            joke = Jokes(
                user_name=form.cleaned_data["user_name"],
                joke_text=form.cleaned_data["joke_text"],
                rating=form.cleaned_data["rating"],
            )
            joke.save()
            return HttpResponseRedirect("/thank-you")

    form = JokeForm()

    # jinak se zobrazi stranka s formularem = původní načtení stránky
    return render(request, "jokesapp/index.html", {"jokeForm": form})


def thank_you(request):
    return render(request, "jokesapp/thank-you.html")

