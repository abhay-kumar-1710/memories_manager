from django.shortcuts import render, redirect, HttpResponseRedirect
from myapp.forms import ImageUploaderForm, UserLogInForm
from myapp.models import ImageUploader
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# HOME
def home(request):
    data = ImageUploader.objects.all().order_by("-id")
    if request.method == "POST":
        form = ImageUploaderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ImageUploaderForm()
    return render(request, 'myapp/home.html', {"form" : form, 'data' : data})

# ABOUT
def about(request):
    return render(request, 'myapp/about.html')

# SHOW-FULL-IMAGE
def showfullimage(request, id):
    data = ImageUploader.objects.get(pk = id)
    return render(request, 'myapp/fullimage.html', {'data' : data})

# DELETE
def delete(request, id):
    data = ImageUploader.objects.get(pk=id)
    data.delete()
    return redirect('/')

# LOGIN
def loginuser(request):
    if request.method == "POST":
        form = UserLogInForm(request = request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
    else:
        form = UserLogInForm()
    return render(request, 'myapp/login.html', {"form":form})

# LOGOUT
def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect('/')