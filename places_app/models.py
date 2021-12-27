from django.conf import settings
from django.db import models
import datetime

class PlaceToRemember(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place_name = models.CharField(verbose_name='Название', max_length=150)
    text = models.TextField(verbose_name='Комментарий')
    address = models.CharField(verbose_name='Адрес', max_length=100, null=True, blank=True)
    pub_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.place_name