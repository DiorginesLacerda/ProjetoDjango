from django.contrib import admin
# Importa o modelo 
from .models import Post

#seta o modelo a ser administrado
admin.site.register(Post)

