from django.shortcuts import render, redirect
from .models import Wiki
from .forms import WikiForm

def index(request):
    return render(request,'main/index.html')

def wiki(request, name):
    wiki = Wiki.objects.get(name=name)
    return render(request, 'main/wiki.html', {'wiki':wiki})

def view_redirect(request):
    name = request.GET.get('name')
    if name:
        if Wiki.objects.filter(name=name).exists():
            return redirect(f'/{name}/')
        else:
            return render(request, 'main/not_found.html')

def edit(request, name):
    wiki = Wiki.objects.get(name=name)

    if request.method == 'POST':
        form = WikiForm(request.POST, instance=wiki)
        if form.is_valid():
            form.save()
            return redirect(f'/{name}/')
    else:
        form = WikiForm(instance=wiki)

    return render(request, 'main/edit.html', {'form':form, 'wiki':wiki})

# Create your views here.
