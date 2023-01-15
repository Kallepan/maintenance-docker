from django.shortcuts import render



def maintenance_view(request, *args, **kwargs):
    context = {
        "time": "12:00",
        "data": ":)",
        "zitat": "Geduld ist eine Tugend, um die Launen des Lebens zu meistern.",
        "autor": "Neufang, Volker"
    }

    return render(request, "index.html", context=context)