from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request, "theally/index.html")


def signup(request):
    if request.method == "POST":
        #username = request.POST.get('username')
        username = request.POST['username']
        emailid = request.POST['emailid']
        password = request.POST['password']
        Cpassword = request.POST['Cpassword']
        referral = request.POST['referral']

        myuser = User.objects.create_user(username,emailid,password)

        myuser.save()

        messages.success(request, "You have been successfully registered.")

        return redirect('signin')
    return render(request, "theally/signup.html")




def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            username = user.username
            return render(request,'theally/index.html', {'username':username})

        else:
            messages.error(request,"Wrong Credentials")
            return redirect('home')





    return render(request, "theally/signin.html")




def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')