from django.db import models

# Create your models here.
class Portifolio(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=150, null=False)
    email = models.EmailField(verbose_name="E-mail", null=False)
    nascimento = models.DateField(verbose_name="Data de Nascimento", null=False)
    RG = models.CharField(verbose_name="RG", max_length=16, null=True)
    CPF = models.CharField(verbose_name="CPF", max_length=16, null=False)

class FormacaoAcademica(models.Model):
    portifolio = models.ForeignKey(verbose_name="Portifólio", null=False)
    inicio = models.DateField(verbose_name="Início", null=False)
    fim = models.DateField(verbose_name="Fim", null=True)
    curso = models.CharField(verbose_name="Curso", null=False)

class Experiencia(models.Model):
    portifolio = models.ForeignKey(verbose_name="Portifólio", null=False)
    inicio = models.DateField(verbose_name="Início", null=False)
    fim = models.DateField(verbose_name="Fim", null=True)
    empresa = models.CharField(verbose_name="Empresa", null=False)