from django.contrib import admin
from .models import LivroModel

# Register your models here.


@admin.register(LivroModel)
class LivroModelAdmin(admin.ModelAdmin):
    pass