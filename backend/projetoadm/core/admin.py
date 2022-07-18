from django.conf import settings
from django.contrib import admin

from .models import Policial, Escala, Posto, Graduacao, VTR,EscalaRegistro,Funcao




@admin.register(Graduacao)
class GraduacaoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'graduacao')
    search_fields = ('graduacao',)


@admin.register(Posto)
class PostoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'posto')
    search_fields = ('posto',)

@admin.register(Funcao)
class FuncaoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'funcao')
    search_fields = ('funcao',)



@admin.register(VTR)
class VTRAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'codigo')
    search_fields = ('codigo',)


@admin.register(Policial)
class PolicialAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'nome', 'sobrenome',
                    'rg_militar', 'cpf', 'graduacao', 'posto')
    search_fields = ('nome', 'sobrenome', 'rg_militar')

    def has_delete_permission(self, request, obj=None):
        if request.user.username == 'admin':
            return True
        return False

class EscalaRegistroInline(admin.TabularInline):
    model = EscalaRegistro
    extra: 0

@admin.register(Escala)
class EscalaAdmin(admin.ModelAdmin):
    inlines = (EscalaRegistroInline, )

    list_display = ('data_inicio', 'semana', 'hora_inicial',
                    'hora_final', 'horas_total', 'vtr',  'rai',)
    search_fields = ('rai', 'data_inicio', 'data_final',
                     'hora_inicial', 'hora_final', 'horas_total')

    def has_delete_permission(self, request, obj=None):
        if request.user.username == 'admin':
            return True
        return False


@admin.register(EscalaRegistro)
class EscalaRegistroAdmin(admin.ModelAdmin):
    

    list_display = ('policial',)

    def has_delete_permission(self, request, obj=None):
        if request.user.username == 'admin':
            return True
        return False
