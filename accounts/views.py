from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render
# from . import forms


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # form = forms.CustomUserCreationForm(request.POST)
        if  form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
        # form = forms.CustomUserCreationForm()
    return render(request, "accounts/signup_page.html", {'form':form }) 


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        # form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
                


    else:
        form = AuthenticationForm()
        # form = forms.LoginForm()
    return render(request,"accounts/login.html", {'form': form}) 

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')
