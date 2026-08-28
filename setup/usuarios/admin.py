from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ['username', 'email', 'perfil', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Informações do LEEPER', {'fields': ('perfil', 'curso', 'turma', 'matricula', 'departamento')}),
    )

admin.site.register(Usuario, CustomUserAdmin)