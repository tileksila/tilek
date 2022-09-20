from datetime import datetime
from distutils.command.upload import upload
from importlib import import_module
from pyexpat import model
from selectors import SelectSelector
from tabnanny import verbose
import turtle
from django.db import models
from django.forms import ImageField




class Student(models.Model):
    fio = models.CharField(max_length=255, verbose_name='Ф.N.0')
    class1 = models.CharField(verbose_name='класс')
    number = models.ImageField(verbose_name='номера родителей')
    location = models.CharField(max_length=127, verbose_name='местоположения')
    photo = ImageField(upload_to='avatar_images/', verbose_name='фото')

    def __str__(self) -> str:
        return self.fio

    class Meta:
        verbose_name = 'ученик'
        verbose_name_plural = 'ученики'

class lessons(models.Model):
    name_less = models.CharField(max_length=255, verbose_name='название уроков')
    teacher = models.CharField(max_length=255, verbose_name='учитель')

    def __str__(self) -> str:
        return self.name_less

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

class Class(models.Model):
    bukva_class = models.CharField(max_length=255, verbose_name='буква класса')
    number_class = models.IntegerField(verbose_name='название класса')
    class_teacher = models.CharField(max_length=255, verbose_name='ФИО')

    def __str__(self) -> str:
        return self.number_class

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

class School(models.Model):
    school_name = models.CharField(max_length=255, verbose_name='Названия школы')
    director = models.CharField(max_length=255, verbose_name='ФИО')
    head_teacher = models.CharField(max_length=255, verbose_name='ФИО')
    teacher = models.CharField(max_length=255, verbose_name='ФИО')
    klass = models.CharField(max_length=255, verbose_name='классы')
    student = models.CharField(max_length=255, verbose_name='ФИО')
    lessons = models.CharField(max_length=255, verbose_name='уроки')

    def str(self):
        return self.school_name

    class Meta:
        verbose_name = 'школа'
        verbose_name_plural = 'школы'


class Director(models.Model):
    fio_director = models.CharField(max_length=255, verbose_name='ФИО')
    foto_director = models.ImageField(upload_to='avatar_images/', verbose_name='фото')
    number_director =  models.IntegerField (verbose_name='номер директора ')

    def str(self):
        return self.fio_director

    class Meta:
        verbose_name = 'директор'
        verbose_name_plural = 'директоры'

class Head_teacher(models.Model):
    fio_h_teacher = models.CharField(max_length=255, verbose_name='ФИО') 
    foto_head_teacher = models.ImageField(upload_to='avatar_images/', verbose_name='фото')
    number_head_teacher =  models.IntegerField (verbose_name='номер зауча')

    def str(self):
        return self.fio_h_teacher

    class Meta:
        verbose_name = 'зауч'
        verbose_name_plural = 'заучи'


class Teacher(models.Model):
    fio_teacher = models.CharField(max_length=255, verbose_name='ФИО') 
    address_teacher = models.CharField(max_length=255, verbose_name='место проживание')
    number_head_teacher = models.IntegerField (verbose_name='номер учителя') 
    foto_teacher = models.ImageField(upload_to='avatar_images/', verbose_name='фото')

    def str(self):
        return self.fio_teacher

    class Meta:
        verbose_name = 'учитель'
        verbose_name_plural = 'учителя'