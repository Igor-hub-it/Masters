from django.db import models

class Master(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    price = models.IntegerField(verbose_name='минимальный прайс')
    photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'