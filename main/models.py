from django.db import models
from django.contrib.auth.models import AbstractUser


sex_choices = (
    ('Мама', 'Мама'),
    ('Папа', 'Папа')
)


class Child(models.Model):
    avatar = models.ImageField(upload_to='/media/kids', verbose_name='Фото Ребенка')
    kids_first_name = models.CharField(max_length=255, verbose_name='Имя Ребенка')
    kids_last_name = models.CharField(max_length=255, verbose_name='Фамилия Ребенка')
    birth_date = models.DateField()

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'

    def __str__(self):
        return f'{self.kids_first_name} {self.kids_last_name}'


class Parent(AbstractUser):
    child = models.ManyToManyField(Child, verbose_name='Ребенок')
    sex = models.CharField(choices=sex_choices, verbose_name='Пол')

    class Meta:
        verbose_name = 'Родитель'
        verbose_name_plural = 'Родители'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
