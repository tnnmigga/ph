from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']
        try:
            User.objects.get(username=username)
            return render(request,'signup.html',{'usernameExist':'用户名已存在'})
        except User.DoesNotExist:
            if password==confirm:
                User.objects.create_user(username=username,password=password)
                return redirect('home')
            else:
                return render(request,'signup.html',{'WrongPassword':'密码错误'})

