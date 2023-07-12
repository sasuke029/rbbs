from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from . models import Note,Room ,Department, Semester,cart
from django.contrib.auth.models import  User
from .forms import MyUserCreationForm, NoteForm

# Create your views here.
def index(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q)  |
        Q(name__icontains=q)
    )
    rooms_count = rooms.count
    topics = Note.objects.all()[0:5]
    context={'rooms':rooms,'topics':topics,'rooms_count':rooms_count}
    return render(request,'index.html',context)


@login_required(login_url='login')
def download_section(request,pk):
    rooms = Room.objects.get(id=pk)
    user =  rooms.host
    similarnote = Room.objects.filter(host = user)
    context={'rooms':rooms,'similarnote':similarnote}
    return render(request,'download_section.html',context)


def profilePage(request,pk):
    user=User.objects.get(id=pk)
    rooms = user.room_set.all() # type: ignore
    topics=Note.objects.all()
    rooms_count = rooms.count
    context = {'user':user,'rooms':rooms,'topics':topics,'rooms_count':rooms_count}
    return render(request,'profile.html',context)

def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'login_register.html', {'form': form})


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'login_register.html', context)




def logoutUser(request):
    logout(request)
    return redirect('home')
    

@login_required(login_url='login')
def createNote(request):
    form = NoteForm()
    topics = Note.objects.all()

    if request.method == "POST":
        topic_name = request.POST.get('topic')
        topic ,created = Note.objects.get_or_create(name=topic_name)

        Room.objects.create(
            topic=topic,
            host=request.user,
            name= request.POST.get('name'),
            description= request.POST.get('description'),
            avatar=request.POST.get('avatar')
        )
        return redirect('home')

    context={'topics':topics,'form':form}
    return render(request, 'create_note.html', context)





def Catagories(request):
    departments = Department.objects.all()
    context = {'departments':departments}
    return render(request,'catagories.html',context)


# def semester(request,pk):
#     department = Department.objects.get(id=pk)
#     semesters = department.semester_set.all() # type: ignore
#     context = {'semesters':semesters}
#     return render(request,'semester.html',context)


def Cart(request):
    if request.method=="POST":
     
         Subjects = request.POST['name']
         Rate=request.POST['email']
         Quantity=request.POST['address']
         Total_Price=request.POST['message']
         data = cart.objects.create(Subjects=Subjects,Rate=Rate,Quantity=Quantity,Total_Price=Total_Price)
    my_cart = cart.objects.all()
    return render(request,'my_cart.html',{'Addtocart':my_cart})

def checkout(request):
    context ={}
    return render(request,'checkout.html',context)
