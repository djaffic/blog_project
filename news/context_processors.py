from .models import Category

def categories_all(request):
    return {"categories": Category.objects.all()}
    #filter(parent__isnull=True)}