from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.http import HttpResponse ,  HttpResponseRedirect
from .models import User
from .forms import SignUpForm






def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            User = form.save()
            get_username = request.POST.get('username')
            get_full_name = request.POST.get('full_name')
            get_email = request.POST.get('email')
            get_password = request.POST.get('password')
            get_password2 = request.POST.get('password2')
            if get_password == get_password2:
                user = User.objects.create_user(
                    username=get_username,
                    full_name = get_full_name,
                    email=get_email,
                    password=get_password,
                    conform_password=get_password2
                    )
                login(request, user)
                print(user)
                return HttpResponse  ("/")
            else:
                error = " Password Mismatch "
                return render(request, 'registration/login_signup.html', {"error": error})

        else:
            error = " Password Mismatch "
            return render(request, 'registration/login_signup.html', {"error": error})
    else:
        form = SignUpForm()

        return render(request, 'registration/login_signup.html',{'form':form})
