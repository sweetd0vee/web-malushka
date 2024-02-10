from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import LoginForm

# Create your views here.

User = get_user_model()


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect("/")
        # attempt = request.sessison.get("attempt") or  0
        # request.session['attempt'] = attempt + 1
        # return redirect("/invalid-password")
        request.session["invalid_user"] = 1  # 1 as True
    return render(request, "accounts/authorization.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/login")
