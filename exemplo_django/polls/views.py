from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Abre o arquivo com o documento HTML, lê todo o conteúdo e fecha o arquivo
indexFile = open("./../html/index.html", "r", encoding="UTF-8")
indexContent = indexFile.read()
indexFile.close()

def index(request):
    return HttpResponse(indexContent)
