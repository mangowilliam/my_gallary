from django.shortcuts import render
from.models import Image


# Create your views here.
def gallary(request):
    mygallary = Image.get_images()
    return render(request, "gallaries/gallary.html", {"mygallary":mygallary})

def search_image(request):
    
    if 'category' in request.GET and request.GET["category"]:
        items = request.GET.get("category")
        searched_images = Image.search_image(item)
        message = f"{item}"

        return render(request, 'gallaries/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any item"
        return render(request, 'gallaries/search.html',{"message":message})

def get_image_by_id(request,image_id):
    try:
        details = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"gallaries/details.html", {"details":details})