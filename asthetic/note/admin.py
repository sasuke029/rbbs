from django.contrib import admin
from .models import Note ,Room,Departments,Semester,Customer,Cart,CartProduct,Order

# Register your models here.
admin.site.register(Note)
admin.site.register(Room)
admin.site.register(Departments)
admin.site.register(Semester)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Order)




