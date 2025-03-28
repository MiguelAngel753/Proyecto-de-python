from django.contrib import admin
from .models import Recurso
from .models import Recurso, SolicitudRecurso

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "cantidad_total", "cantidad_disponible", "fecha_creacion")
    search_fields = ("nombre", "tipo")
    list_filter = ("tipo", "fecha_creacion")

@admin.register(SolicitudRecurso)
class SolicitudRecursoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "recurso", "cantidad_solicitada", "fecha_solicitud", "estado")
    list_filter = ("estado", "fecha_solicitud")
    search_fields = ("usuario__username", "recurso__nombre")
    