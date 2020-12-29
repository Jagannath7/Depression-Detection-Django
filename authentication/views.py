from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import User_Data
# Create your views here.



def home(request):

    return render(request, 'home.html')


def signin(request):
    if request.method == 'POST':
        global name
        name = request.POST['name']
        password = request.POST['password']
        

        user = auth.authenticate(username=name, password=password)

        if user is  None:
            messages.info(request, 'invalid credentials')
            print('maddy sexy')
            return redirect('signin')
        else:
            auth.login(request, user)
            return redirect("/",)

    else:
        return render(request,'signin.html')    

def signup(request):

   
    if request.method == 'POST':
        username = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']
        

        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Taken')
            return redirect('signup')
        else:   
            user = User.objects.create_user(password=password,username=username, email=email)
            user.save()
            user_data = User_Data(name=username, contact=contact, email=email)
            user_data.save()
            print('user created')
            return redirect('/signin')

        
    else:
        return render(request, 'signup.html')

@login_required(login_url='/signin')
def signout(request):
    auth.logout(request)
    print("signed out")
    return redirect('/signin')    

def data(request):
    return HttpResponse('hello')
    
def about(request):
    return render(request, 'about.html')

@login_required(login_url='/signin')
def myaccount(request):
    user_data = request.user
    userData = User_Data.objects.get(name=user_data.username)
    return render(request, 'account.html', {'name':userData.name, 'email':userData.email, 'contact':userData.contact})

@login_required(login_url='/signin')
def edit(request):
    if request.method == "POST":
        user_data_edit = User.objects.get(username=request.user.username)
        userDataEdit = User_Data.objects.get(name=user_data_edit.username)
        name_ = request.POST['name']
        email_ = request.POST['email']
        contact_ = request.POST['contact']
       
        user_data_edit.username = name_
        user_data_edit.email = email_
        userDataEdit.name = name_
        userDataEdit.email = email_
        userDataEdit.contact = contact_
        user_data_edit.save()
        userDataEdit.save()
        return render(request, 'edit.html',{'name':userDataEdit.name, 'email':userDataEdit.email, 'contact':userDataEdit.contact})
    else:
        user_data_edit = request.user
        userDataEdit = User_Data.objects.get(name=user_data_edit.username)
        return render(request, 'edit.html', {'name':userDataEdit.name, 'email':userDataEdit.email, 'contact':userDataEdit.contact})


def passwordReset(request):
    if request.method == 'POST':
        username = request.POST['name']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                user_info = User.objects.get(username=username)
                user_info.set_password(password1)
                user_info.save()
                messages.info(request, "Password changed successfully")
                return redirect('/signin')
            else:
                messages.info(request, "User does not exist")
                return redirect('/passwordreset')
        else:
            messages.info(request, "Password don't match")
            return redirect('/passwordreset')
    else:
        
        return render(request, 'passwordReset.html')