from django.db import models
from django.contrib.auth.models import User





class Note(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


    

class Departments(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Semester(models.Model):
    department = models.ForeignKey(Departments , on_delete=models.CASCADE)
    name=models.CharField(max_length=100)


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Note, on_delete=models.SET_NULL, null=True)
    rate = models.PositiveIntegerField(null=True)
    department=models.ForeignKey(Departments,on_delete=models.CASCADE)
    semester= models.ForeignKey(Semester, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, default="avatar.svg")
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address=models.CharField(max_length=200,blank=True,null=True)
    joined_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
       
       return self.full_name


    
class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    total=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)


class CartProduct(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Room,on_delete=models.CASCADE)
    rate=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    subtotal=models.PositiveIntegerField()

    def __str__(self):
        return 'cart' + str(self.cart.id) + 'cartproduct' + str(self.id) # type: ignore


ORDER_STATUS =(
    ('Order Received','Order Received'),
    ('Order Processing','Order Processing'),
    ('On the way','On the way'),
    ('Order Completed','Order Completed'),
    ('Order Canceled','Order Canceled'),
)
METHOD =(
    ("Cash On Delivery","Cash On Delivery"),
    ("Esewa",'Esewa'),
)

class Order(models.Model):
    cart=models.OneToOneField(Cart,on_delete=models.CASCADE)
    ordered_by=models.CharField(max_length=200)
    shipping_address=models.CharField(max_length=200)
    mobile=models.CharField(max_length=10)
    email=models.EmailField(null=True,blank=True)
    subtotal=models.PositiveIntegerField()
    discount=models.PositiveIntegerField()
    total=models.PositiveIntegerField()
    order_status=models.CharField(max_length=50,choices=ORDER_STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    payment_method=models.CharField(max_length=20,choices=METHOD,default="Cash On Delivery")
    payment_completed=models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return 'Order' + str(self.id) # type: ignore

