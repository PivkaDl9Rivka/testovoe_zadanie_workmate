from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Breed(models.Model):
    breed = models.CharField(verbose_name='Название породы', max_length=16,)


class Cat(models.Model):
    color = models.CharField(
        verbose_name='Цвет кошки',
        max_length=16,
    )
    age = models.IntegerField(
        verbose_name='Возраст кошки',
    )
    description = models.TextField(
        verbose_name='Описание кошки',
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE,
        related_name='breed_cat',
    )
    owner = models.ForeignKey(
        User,
        related_name='user_cat',
        on_delete=models.CASCADE,
        verbose_name='Владелец кошки',
    )
