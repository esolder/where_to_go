from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


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


class Image(models.Model):
    place = models.ForeignKey(Place,
                              on_delete=models.CASCADE,
                              related_name='images',
                              verbose_name='Место')
    image = models.ImageField('Изображение')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.id} {self.place.title}'


@receiver(pre_delete, sender=Image)
def delete_image(sender, instance, **kwargs):
    instance.image.delete()