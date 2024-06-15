from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import Room, Topic
from .forms import RoomForm, UpdateForm
# Create your views here.
# rooms = [
#     {'id' : 1, 'name' : 'lets learn python'},
#     {'id' : 2, 'name' : 'Design with me'},
#     {'id' : 3, 'name' : 'Frontend Developer'},
# ]



def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {'rooms':rooms, 'topics': topics, 'room_count':room_count}
    return render(request, "base/home.html", context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, "base/room.html", context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id = pk)
    form = UpdateForm(instance=room)
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context= {'form': form}
    return render(request, 'base/room_form.html', context=context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnot exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password doesnot exist')
    context={}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')