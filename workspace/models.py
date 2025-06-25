from django.db import models
from shared.models import Base
from django.contrib.auth.models import User


class WorkSpace(Base):
    user = models.ForeignKey(User, verbose_name='usuário', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Título', max_length=255)

    class Meta:
        verbose_name = 'Espaço de trabalho'
        verbose_name_plural = 'Espaços de trabalhos'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.user}"
