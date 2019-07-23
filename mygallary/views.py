from django.shortcuts import render

from.models import Image


# Create your views here.
def gallary(request):
    mygallary = Image.get_images()
    return render(request, "gallaries/gallary.html", {"mygallary": mygallary})


def search_image(request):

    if 'images' in request.GET and request.GET["images"]:
        items = request.GET.get("images")
        searched_images = Image.search_image(items)
        print(searched_images)
        message = f"{items}"

        return render(request, 'gallaries/search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any item"
        return render(request, 'gallaries/search.html', {"message": message})


def get_image_by_id(request, image_id):
    try:
        details = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "gallaries/details.html", {"details": details})

def search_location(request):
    if 'images' in request.GET and request.GET["images"]:
        location = request.GET.get("images")
        searched_images = Image.search_location(location)
        print(searched_images)
        message = f"{location}"

        return render(request, 'gallaries/details.html', {"message": message, "images": searched_images})