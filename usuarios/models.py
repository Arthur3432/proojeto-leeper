from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    PERFIL_CHOICES = (
        ('ALUNO', 'Aluno'),
        ('PROFESSOR', 'Professor / Moderador'),
    )
    perfil = models.CharField(max_length=10, choices=PERFIL_CHOICES, default='ALUNO')
    
    # Atributos específicos do Aluno
    curso = models.CharField(max_length=100, blank=True, null=True)
    turma = models.CharField(max_length=50, blank=True, null=True)
    
    # Atributos específicos do Professor
    matricula = models.CharField(max_length=50, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)

    def is_professor(self):
        return self.perfil == 'PROFESSOR' or self.is_superuser

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_perfil_display()})"