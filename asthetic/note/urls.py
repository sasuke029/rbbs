from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('/download_section/<str:pk>/',views.download_section,name="download_section"),
    path('/login',views.loginPage,name="login"),
    path('/register',views.registerPage,name="register"),
    path('/logout',views.logoutUser,name="logout"),
    path('/createNote',views.createNote,name="create-note"),
    path('/logout',views.logoutUser,name="logout"),
    path('/my_cart',views.Addtocart,name="Addtocart"),
    path('/checkout',views.Checkout,name="checkout"),

]