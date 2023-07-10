from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def user_register(request):
     if request.method == 'GET':
        return render(request, 'auth_app/register.html')
     
     else:
       badri = User.objects.all()
       print('&&&&&&&')
       print(badri)
       fn = request.POST['firstname']
       ln = request.POST['lastname']
       username = request.POST['username']
       email = request.POST['email']
       pswd = request.POST['password']
       User.objects.create_user(first_name=fn, last_name=ln, username=username, email=email, password=pswd)
       messages.success(request, 'User created successfully!!')
       return redirect('authapp-login')

def user_login(request):
    if request.method == 'GET':
        return render(request, 'auth_app/login.html')
    
    else:
      uname = request.POST['username']
      pswd = request.POST['password']
      user = authenticate(request, username=uname, password=pswd)
      if user is not None:
         login(request, user)
         messages.success(request, 'You are successfully Login, Thank You!!')
         return redirect('mainapp-home')

      else:
         messages.success(request, 'your credencials does not match!!')
      return render(request, 'auth_app/login.html')
    #    login = User.objects.all()
    #    print(login)


def user_logout(request):
    logout(request)
    return redirect('authapp-login')


  #    print('********')
    #    print(request.POST['firstname'])
    #    print(make_password(pswd))