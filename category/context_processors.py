from .models import Category

def menu_links(request):
    """
    Context processor to add menu links to the context.
    """
    categories = Category.objects.all()
    return {'categories': categories}