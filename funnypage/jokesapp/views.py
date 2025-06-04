from django.shortcuts import render


# Create your views here.
def jokes(request):
    # podmínka pokud se odešle formulář, tak se zobrazi stranka s dekujem
    if request.method == "POST":
        visiter_name = request.POST["username"]
        print(visiter_name)  # pro testování jestli se nám vrací data
        return render(request, "jokesapp/thank-you.html")

    # jinak se zobrazi stranka s formularem
    return render(request, "jokesapp/index.html")

