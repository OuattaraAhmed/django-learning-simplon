from django.shortcuts import render, redirect
from .models import Simploniens

# Create your views here.
def index(request):
    title = 'Accueil'
    simploniens = Simploniens.objects.all()
    return render(request, 'sitedjangoapp/home.html', {'title': title, 'simploniens': simploniens})

def contact(request):
    contact_title = 'Contact'
    return render(request, 'sitedjangoapp/contact.html', { 'title': contact_title })


def supprimer(request, id):
    getID = Simploniens.objects.get(pk=id)

    if request.method == 'POST':
        return getID.delete()
    return redirect('home')