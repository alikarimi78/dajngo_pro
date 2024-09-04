from django.contrib import admin
from users.models import Person
# Register your models here.

@admin.register(Person)
class ModelNameAdmin(admin.ModelAdmin):
    pass