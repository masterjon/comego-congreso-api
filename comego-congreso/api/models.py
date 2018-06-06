# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField


class CategoryItem(models.Model):
    title = models.CharField(max_length=50)
    picture = models.ImageField(null=True, blank=True)
    ordering = models.PositiveSmallIntegerField(default=0)
    link = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Categorias'
        ordering = ['ordering']

    def __str__(self):
        return self.title


class ActivityCategory(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(CategoryItem, related_name='activity_category', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Categorias de Actividades'

    def __str__(self):
        return self.title


class Salon(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Salones'

    def __str__(self):
        return self.title


class Actividad(models.Model):
    dress_options = (
        ('formal', 'Formal',),
        ('casual', 'Casual',)
    )
    category = models.ForeignKey(ActivityCategory, related_name='actividades', on_delete=models.CASCADE)
    title = models.CharField('Título', max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = RichTextField()
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    dress_code = models.CharField('Código de vestir', choices=dress_options, max_length=50)
    academic_program_url = models.URLField('Url Programa Académico', blank=True)
    inscription_url = models.URLField('Url Inscripción', blank=True)
    ordering = models.PositiveSmallIntegerField(default=0)
    month = models.CharField(max_length=50, null=False, blank=True, default='')

    class Meta:
        verbose_name_plural = 'Actividades'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.month = self.start_date.strftime("%B")
        super(Actividad, self).save(*args, **kwargs)


class Sponsor(models.Model):
    title = models.CharField('Título', max_length=50)
    description = models.TextField(blank=True)
    link = models.URLField()
    picture = models.ImageField(null=True, blank=True)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title


class Asistente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s".format(self.nombres, self.apellidos)


class ProfesorCategory(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categorias de Profesores'

    def __str__(self):
        return self.title


class Profesor(models.Model):
    category = models.ForeignKey(ProfesorCategory, related_name='profesores', on_delete=models.CASCADE)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    picture = models.ImageField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "{} {}".format(self.nombres, self.apellidos)
