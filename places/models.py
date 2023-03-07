from django.db import models


class Place(models.Model):
    title = models.CharField('Название места', max_length=200)
    description_short = models.CharField('Краткое описание', max_length=300)
    description_long = models.TextField('Подробное описание')
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title  