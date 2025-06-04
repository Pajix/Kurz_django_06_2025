from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import JokeForm  # import z forms.py který jsme si vytvorili a je tam template pro formular


# Create your views here.
def jokes(request):
    # podmínka pokud se odešle formulář, tak se zobrazi stranka s dekujem
    if request.method == "POST":
        form = JokeForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # pro testování jestli se nám vrací data
            return HttpResponseRedirect("/thank-you")

    form = JokeForm()

    # jinak se zobrazi stranka s formularem = původní načtení stránky
    return render(request, "jokesapp/index.html", {"jokeForm": form})


def thank_you(request):
    return render(request, "jokesapp/thank-you.html")

