from django.db import models

class Master(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    price = models.IntegerField(verbose_name='минимальный прайс')
    photo = models.ImageField(upload_to='photos', blank=True)
    experience = models.IntegerField(default=0)
    phone = models.CharField(max_length=12, blank=True)
    vk = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'