from django.db import models


class Child(models.Model):
    kids_first_name = models.CharField(max_length=255, verbose_name='Имя Ребенка')
    fathers_name = models.CharField(max_length=255, verbose_name='Имя Отца')
    mothers_name = models.CharField(max_length=255, verbose_name='Имя Матери')
    birth_date = models.DateField()

