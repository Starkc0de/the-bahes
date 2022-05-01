from django.shortcuts import redirect, render
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class LoginPageView(generic.TemplateView):
    template_name = "accounts/login.html"

    def post(self, request,*args, **kwargs):
        if request.method == "POST":
            form = User(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.info(
                    request, f"You are now logged in as {username }.")  
                if request.user.is_authenticated:                       
                    return render(request, "dashboard/profile.html")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
        form = User()
        return render(request, "accounts/login.html", {'form': form})


class RegistraionPageView(generic.TemplateView):
    template_name = "accounts/registration.html"
    form1 = UserForm()
    form2 = RegisterForm()

    def post(self, request,):
        if request.method == 'POST':
            form1 = UserForm(request.POST, request.FILES,)
            form2 = RegisterForm(request.POST, request.FILES,)
            if form1.is_valid():
                if form2.is_valid():
                    saveform1 = form1.save()
                    saveform1.save()
                    saveform2 = form2.save(commit=False)
                    saveform2.user = saveform1
                    saveform2.save()
                    # login(self.request, UserForm,)
                    messages.success(
                        request, f'Your account has been created ! You are now able to log in')
                return render(request, "accounts/registration.html")
        else:
            form1 = UserForm()
            form2 = RegisterForm()
            messages.error(
                request, f'Your account has not created ! You fill the right information')
        return render(request,  "accounts/registration.html", {'form1': form1})


class ForgotPageView(generic.TemplateView):
    template_name = "accounts/forgot.html"


@login_required
def LogoutPageView(request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return render(request, "accounts/login.html" )


