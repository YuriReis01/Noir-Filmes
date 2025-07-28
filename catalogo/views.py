from django.shortcuts import render, redirect, get_object_or_404
from .models import Filme
from .forms import FilmeForm
import requests

# Sua chave da TMDb (não esquece das aspas!)
TMDB_API_KEY = "d6b193594c2cd26c293460d4ffd6bc16"


def buscar_poster(titulo):
    url = 'https://api.themoviedb.org/3/search/movie'
    params = {
        'api_key': TMDB_API_KEY,
        'query': titulo,
        'language': 'pt-BR'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        resultados = data.get('results')
        if resultados:
            poster_path = resultados[0].get('poster_path')
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return None


def lista_filmes(request):
    filmes = Filme.objects.all().order_by('-id')
    return render(request, 'catalogo/lista_filmes.html', {'filmes': filmes})


def adicionar_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            filme = form.save(commit=False)
            poster = buscar_poster(filme.titulo)
            if poster:
                filme.poster_url = poster
            filme.save()
            return redirect('lista_filmes')
    else:
        form = FilmeForm()
    return render(request, 'catalogo/form_filme.html', {'form': form})


def editar_filme(request, filme_id):
    filme = get_object_or_404(Filme, pk=filme_id)
    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            filme = form.save(commit=False)
            poster = buscar_poster(filme.titulo)
            if poster:
                filme.poster_url = poster
            filme.save()
            return redirect('lista_filmes')
    else:
        form = FilmeForm(instance=filme)
    return render(request, 'catalogo/form_filme.html', {'form': form})


def excluir_filme(request, filme_id):
    filme = get_object_or_404(Filme, pk=filme_id)
    filme.delete()
    return redirect('lista_filmes')
