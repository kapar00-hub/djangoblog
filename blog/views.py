from django.shortcuts import render


def home(request):
    return render(request, 'blog/home.html',
                  {'title': 'Hello Djangoblog'
    })


def about(request):
    return render(request, "blog/about.html", 
                  {"title": "This is the DjangoBlog Team"})


def base(request):
    return render(request, "blog/base.html",
                 {"title": "This is the DjangoBlog Team"})

def contact(request):
    return render(request, "blog/contact.html", 
                  {"title": "This is the DjangoBlog Team"})
