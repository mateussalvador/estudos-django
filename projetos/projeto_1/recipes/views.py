from django.shortcuts import render

def home(request):
    return render(request, 'recipes/pages/home.html', context={"name": "Salvador"})

def recipes(request, id):
    return render(request, 'recipes/pages/recipes_view.html')
