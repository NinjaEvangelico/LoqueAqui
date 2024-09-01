from django.shortcuts import render, redirect, get_object_or_404
from .models import Anuncio
from .forms import AnuncioForm

def home(request):
    anuncios = Anuncio.objects.all().order_by('-data_criacao')
    return render(request, 'anuncios_s/home.html', {'anuncios': anuncios})

def novo_anuncio(request):
    if request.method == 'POST':
        form = AnuncioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AnuncioForm()
    return render(request, 'anuncios_s/novo_anuncio.html', {'form': form})

def editar_anuncio(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    if request.method == 'POST':
        form = AnuncioForm(request.POST, request.FILES, instance=anuncio)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AnuncioForm(instance=anuncio)
    return render(request, 'anuncios_s/editar_anuncio.html', {'form': form, 'anuncio': anuncio})

def deletar_anuncio(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    if request.method == 'POST':
        anuncio.delete()
        return redirect('home')
    return render(request, 'anuncios_s/deletar_anuncio.html', {'anuncio': anuncio})
