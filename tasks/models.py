from django.db import models
from django.contrib.auth.models import User

from shared.models import Base
from workspace.models import WorkSpace


class Task(Base):
    STATUS_CHOICES = (
        ('Done', 'Concluido'),
        ('To do', 'À fazer'),
        ('In progress', 'Andamento'),
        ('Paused', 'Pausado')
    )
    PRIORITY_CHOICES = (
        ('Low', 'Baixa'),
        ('Medium', 'Média'),
        ('High', 'Alta'),
        ('Urgent', 'Urgente')
    )
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição', null=True, blank=True)
    work_space = models.ForeignKey(WorkSpace, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='Medium', verbose_name='Prioridade')
    completed_at = models.DateTimeField(verbose_name='Concluído em', null=True, blank=True)


    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.user}"