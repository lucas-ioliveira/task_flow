from django.db import models


class Base(models.Model):
    active = models.BooleanField(verbose_name='Ativo', default=True)
    created_at = models.DateTimeField(
        verbose_name='Data de criação',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Data de atualização',
        auto_now=True
    )

    class Meta:
        abstract = True