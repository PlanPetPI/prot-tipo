from django.db import models


class Campanha(models.Model):
    """um assunto sobre o qual o usuario esta aprendendo"""
    text = models.CharField(max_length=200)
    date_add = models.DateField(auto_now=True)

    def __str__(self):
        """devolve uma representação em string do modelo"""
        return self.text


class Entrada (models.Model):
    topico = models.ForeignKey(Campanha, on_delete=models.CASCADE)
    text = models.TextField()
    data_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entradas'

    def __str__(self):
        """devolve uma representação em string do modelo"""
        return self.text[:50] + '...'
