from django.shortcuts import render
from.models import Image


# Create your views here.
def gallary(request):
    mygallary = Image.get_images()
    return render(request, "gallary.html", {"mygallary":mygallary})

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"image": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})