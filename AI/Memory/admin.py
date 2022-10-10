from django.contrib import admin

from .models import Group, Person, Object

# Register your models here.

admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Object)
