from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .forms import BankForm
from django.contrib.auth import authenticate, login as auth_login



# Create your views here.
def login(req):
    if req.method =='POST':
#        return (req,'login.html')
        username=req.POST['username']
        password=req.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(req,user)
            return redirect("regapp:forms")
        else:
            messages.info(req,"invalid")
#            return redirect('login')
    return render(req,'login.html')
def register(val):
    if val.method == 'POST':
        username = val.POST['username']
        password = val.POST['password']
        c_password= val.POST['password1']
        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(val, 'existing username')
                return redirect('regapp:register')
            else:
                user = User.objects.create_user(username=username, password=password)
#                UserProfile.objects.create(user=user)
                user.save();
                auth.login(val, user)
                return redirect('regapp:login')
#                # Create UserProfile for the registered user

        else:
            messages.info(val, 'password not matching')
            return redirect('regapp:register')
        return redirect('/')
    return render(val, "register.html")



def branch(request):
    return render(request, 'branch.html')

def forms(request):
    forms = BankForm()
    return render(request, 'form.html', {'form': forms})

def logout(request):
    auth.logout(request)
    return redirect('/')

def Alappuzha(request):
    return render(request, 'AL.html')
def Ernakulam(request):
    return render(request, 'ER.html')
def Idukki(request):
    return render(request, 'ID.html')
def Kannur(request):
    return render(request, 'KN.html')
def Kasaragod(request):
    return render(request, 'KS.html')
def message(request):
    return render(request, 'message.html')
