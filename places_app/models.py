from django.conf import settings
from django.db import models


class PlaceRemember(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    place_name = models.CharField(
        max_length=150,
        verbose_name='Название'
    )
    comment = models.TextField(
        verbose_name='Комментарий'
    )
    pub_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата'
    )
    

    def __str__(self):
        return self.place_name
    
    class Meta:
        verbose_name = 'Воспоминание'
        verbose_name_plural = 'Воспоминания'
