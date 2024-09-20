from django.contrib import admin
from .models import Livro

class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome','autor', 'ano')
    list_filter = ['ano',]
    search_fields = ['nome', 'autor',]
admin.site.register(Livro, LivroAdmin)