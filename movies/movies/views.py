from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from userformdata.models import MovieBooking
def home(request):
    return render(request,'index.html')
def userform(request):
    if request.method == 'POST':
        moviename=request.POST.get('movie')
        uname = request.POST.get('name')
        uemail = request.POST.get('email')
        ticket = request.POST.get('quantity')
        date = request.POST.get('date')
        time=request.POST.get('time')
        en =MovieBooking(  movie = moviename, name= uname, email= uemail,quantity=ticket,date=date,time= time )
        en.save()
    return render(request,'userform.html')

def view(request):
    formdata= MovieBooking.objects.all()
    data={
        'data':formdata
    }
    return render(request,'view.html',data)

def singup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists!")
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already exists!")
        
        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    
    return render(request, 'singup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('view')  # Replace 'view' with the name of the view you want to redirect to after successful login
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username and/or password.'})
    return render(request, 'login.html')



   
    
