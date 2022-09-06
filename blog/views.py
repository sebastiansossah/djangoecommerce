from django.shortcuts import render
from blog.models import post, categories

# Create your views here.

def Blog(request):
    varPost= post.objects.all()
    return render(request, 'Blog/blog.html', {'varPost': varPost})

def category(request, categories_id):
    varCategories= categories.objects.get(id=categories_id)
    varPost= post.objects.filter(category = varCategories)
    return render(request, 'Blog/categories.html', {'varCategories': varCategories, 'varPost': varPost} )

