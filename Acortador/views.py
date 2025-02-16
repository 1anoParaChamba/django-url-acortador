from django.shortcuts import render,redirect,get_object_or_404
from .forms import AcortarNuevaUrl
from .models import UrlAcortadas
from django.contrib import messages
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.http import Http404


def es_url_valida(url):
    validador = URLValidator()
    try:
        validador(url)
        return True
    except ValidationError:
        return False

# Create your views here.
def main(request):
    if request.method=='GET':
        return render(request,'main.html',{'form':AcortarNuevaUrl()})
    else:

        if not es_url_valida(request.POST['url']):
            messages.error(request, "❌ Esta URL no es válida. Intenta con otra.")
            return redirect('/',{'mensaje':'Esta URL no es Valida'})
        if UrlAcortadas.objects.filter(url=request.POST['url']).exists():

            url=UrlAcortadas.objects.filter(url=request.POST['url']).first()
            url_corta=UrlAcortadas.url_acortda(url.codigo)
            messages.info(request, f"⚠️ La URL ya existe: <a href='{url_corta}' target='_blank' class='copyable'>{url_corta}</a> <button class='btn-copy' onclick='copiarTexto(\"{url_corta}\")'>📋 Copiar URL</button>")
            return redirect('/',{'mensaje':'Esta URL ya existe'})
        
        UrlAcortadas.objects.create(url=request.POST['url'])
        url=UrlAcortadas.objects.filter(url=request.POST['url']).first()
        url_corta=UrlAcortadas.url_acortda(url.codigo)
        messages.success(request, f"✅ URL acortada con éxito: <a href='{url_corta}' target='_blank' class='copyable'>{url_corta}</a> <button class='btn-copy' onclick='copiarTexto(\"{url_corta}\")'>📋 Copiar URL</button>")
        return redirect('/')


def redirigir(request, codigo):
    try:
        url = get_object_or_404(UrlAcortadas, codigo=codigo)
        return redirect(url.url)
    except Http404:
        return redirect('/')
                
        




        


    