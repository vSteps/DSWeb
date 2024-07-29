from django.contrib import admin

from .models import Pergunta
from .models import Alternativa

class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 2

class PerguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['texto_pergunta']}),
        ('Informações de data:', {'fields':['data_publicacao']}),
    ]
    inlines = [AlternativaInline]
    list_display = ('texto_pergunta','id', 'data_publicacao', 'foi_publicado_recentemente',)
    list_filter = ['data_publicacao',]
    search_fields = ['texto_pergunta', 'id',]

admin.site.register(Pergunta, PerguntaAdmin)
#admin.site.register(Alternativa)
