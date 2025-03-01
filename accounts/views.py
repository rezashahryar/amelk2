from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import LoginForm, RegisterForm

# Create your views here.


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['mobile'], password=cd['password'])
            if user is not None:
                login(request, user)
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect('pages:home')
    context = {
        'login_form': form
    }
    return render(request, 'accounts/login.html', context)


def register_view(request):
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'حساب کاربری شما با موفقیت ساخته شد')
            return redirect('accounts:login')
        else:
            print(register_form.errors)
    context = {
        'register_form': register_form,
    }
    return render(request, 'accounts/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('pages:home')
