from django.contrib import admin

from .models import Pergunta
from .models import Alternativa

admin.site.register(Pergunta)
admin.site.register(Alternativa)
# Register your models here.
