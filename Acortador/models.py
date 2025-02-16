from django.db import models
import string
import random

def generar_codigo():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
# Create your models here.

class UrlAcortadas(models.Model):
    url=models.TextField(unique=True)
    codigo=models.TextField(max_length=10, unique=True, default=generar_codigo)
    
    
    
    def url_acortda(codigo):
        return f"https://django-url-acortador.onrender.com/{codigo}"


