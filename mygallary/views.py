from django.shortcuts import render


# Create your views here.
def gallary(request):
    return render(request, "gallary.html")
