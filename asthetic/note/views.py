from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import Note,Room
from django.contrib.auth.models import  User
from .forms import MyUserCreationForm, NoteForm

# Create your views here.
def index(request):

    rooms = Room.objects.all()
    context={'rooms':rooms}
    return render(request,'index.html',context)



def download_section(request,pk):
    rooms = Room.objects.get(id=pk)
    roomed= Room.objects.all()
    context={'rooms':rooms,'roomed':roomed}
    return render(request,'download_section.html',context)


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



def Addtocart(request):
    context = {}
    return render(request,'my_cart.html',context)

def Checkout(request):
    context = {}
    return render(request,'checkout.html',context)