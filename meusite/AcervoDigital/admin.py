from django.contrib import admin
from .models import Livro, Item

class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome','autor', 'ano')
    list_filter = ['ano',]
    search_fields = ['nome', 'autor',]
admin.site.register(Livro, LivroAdmin)
admin.site.register(Item)