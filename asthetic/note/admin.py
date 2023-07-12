from django.contrib import admin
from .models import Note ,Room,Department,Semester

# Register your models here.
admin.site.register(Note)
admin.site.register(Room)
admin.site.register(Department)
admin.site.register(Semester)
