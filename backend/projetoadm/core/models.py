
from distutils.archive_util import make_zipfile
from tkinter.tix import Balloon
from django.db import models
from django.forms import CharField
from util.data import SEMANA


# Create your models here.




class Posto(models.Model):
    posto = models.CharField('posto', max_length=50, blank=True, null=True)

    class Meta:
        ordering = ('posto',)
        verbose_name = 'posto'
        verbose_name_plural = 'postos'

    def __str__(self):
        return f'{self.posto}'

    # def to_dict_base(self):
    #     return{
    #        'posto':'self.posto'

    #     }
    


class Graduacao(models.Model):
    graduacao = models.CharField('graduaçao', max_length=50, blank=True, null=True)

    class Meta:
        ordering = ('graduacao',)
        verbose_name = 'graduação'
        verbose_name_plural = 'graduações'

    def __str__(self):
        return f'{self.graduacao}'

class VTR(models.Model):
    placa=models.CharField('placa',max_length=10,null=True,blank=True)
    codigo=models.IntegerField('codigo',null=True,blank=True)

    def __str__(self):
        return f'{self.codigo}' 

class Funcao(models.Model):
    funcao=models.CharField('funcao',max_length=20,null=True,blank=True)

    def __str__(self):
        return self.funcao


class Policial(models.Model):

    nome = models.CharField('nome', max_length=50, null=True)
    sobrenome = models.CharField('sobrenome', max_length=50, null=True)
    rg_militar = models.CharField('rg militar',max_length=8, unique=True, null=True)
    cpf = models.CharField('cpf', max_length=15, unique=True, null=True)
    
    # escala = models.ForeignKey(
    #     'escala',
    #     on_delete=models.SET_NULL,
    #     verbose_name='escala',
    #     related_name='policiais',
    #     null=True,
    #     blank=True
    # )



    posto = models.ForeignKey(
        Posto,
        on_delete=models.CASCADE, 
        null=True,
        blank=True
    )

    graduacao = models.ForeignKey(
        Graduacao,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
  


    def __str__(self):
       return f'{self.cpf} {self.rg_militar} {self.nome} '

    """ def to_dict_base(self):
        return{
            'pk':self.pk,
            'nome':self.nome,
            'sobrenome':self.sobrenome,
            'rg_militar': self.rg_militar,
            'cpf':self.cpf,
            'graduacao':self.graduacao,
            'posto':self.posto

        } """



class Escala(models.Model):
    
    # policial = models.ForeignKey(
    #     'policial',
    #     on_delete=models.SET_NULL,
    #     verbose_name='policial',
    #     related_name='policiais',
    #     null=True,
    #     blank=True
    # )




    rai = models.IntegerField('Rai Escala', blank=False, unique=True)
    data_inicio = models.DateField('data inicial', null=True, help_text='Data no Formato dd/mm/YYYY')
    data_final = models.DateField('data final', null=True, help_text='Data no Formato dd/mm/YYYY')
    hora_inicial = models.TimeField('hora inicial', null=True)
    hora_final = models.TimeField('hora final', null=True)
    horas_total = models.IntegerField('horas', null=True)
    semana=models.CharField('semana',max_length=50,choices=SEMANA,default='segunda')
    


    vtr = models.ForeignKey(
        'vtr',
        on_delete=models.SET_NULL,
        verbose_name='VTR',
        null=True,
        blank=True
    )
    
    
    funcao=models.ForeignKey(
        'funcao',
        on_delete=models.CASCADE,
        verbose_name='funções',
        null=True,
        blank=True
    )
    
    
        # horas_total=(hora_final ) - (hora_inicial)

    def to_dict_base(self):
        return{
            'rai': self.rai,
            'data_inicio': self.data_inicio,
            'data_final': self.data_final,
            'hora_inicial': self.hora_inicial,
            'hora_final': self.hora_final,
            'vtr':self.vtr


        }


class EscalaRegistro(models.Model):

      policial = models.ForeignKey(
        'policial',
        on_delete=models.SET_NULL,
        verbose_name='policial',
        related_name='policiais',
        null=True,
        blank=True
    )

      escala = models.ForeignKey(
        'escala',
        on_delete=models.SET_NULL,
        verbose_name='escala',
        related_name='policiais',
        null=True,
        blank=True
    )
     