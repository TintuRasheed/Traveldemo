from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method=='POST':
        Name=request.POST['Username']
        Email=request.POST['email']
        Password=request.POST['password']
        user=auth.authenticate(username=Name,email=Email,password=Password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Login")
            return redirect('login') 
    return render(request,"Login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
    
def Register(request):
    if request.method=='POST':
        user_n=request.POST['U_name']
        First=request.POST['F_name']
        Last=request.POST['L_name']
        email=request.POST['Email']
        Pass=request.POST['Pass']
        Cpass=request.POST['C_pass']
        
        if Pass==Cpass:
            if User.objects.filter(username=user_n).exists():
                messages.info(request,"Username already Taken")
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already Taken")
                return redirect('Register')
            else:
                user1=User.objects.create_user(username=user_n,first_name=First,last_name=Last,email=email,password=Pass)
                user1.save()
                return redirect('login')
                print("\n--------USER CREATED------------")  
                print('')
        else:
            messages.info(request,"Password not Matching")
            return redirect('Register')
        return redirect('/')
            # print("not match")
    return render(request,"Regi.html")