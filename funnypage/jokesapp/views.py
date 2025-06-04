from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def jokes(request):
    # podmínka pokud se odešle formulář, tak se zobrazi stranka s dekujem
    if request.method == "POST":
        visiter_name = request.POST["username"]
        # pokud se zadal prazdny string
        if visiter_name == "":
            # pokud se zadal prazdny string, tak se zobrazi chyba
            # v html strance pal vložit {% if empty_username %}
            return render(request, "jokesapp/index.html", {"empty_username": True})

        print(visiter_name)
        # pro testování jestli se nám vrací data
        return HttpResponseRedirect("/thank-you")

    # jinak se zobrazi stranka s formularem = původní načtení stránky
    return render(request, "jokesapp/index.html")


def thank_you(request):
    return render(request, "jokesapp/thank-you.html")

