from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

def login(request):
    invalid_login = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                return HttpResponseRedirect('/login/success/')
            else:
                invalid_login = True
    else:
        form = LoginForm()
    return render(request, 'login.html', { 'form': form, invalid_login: invalid_login })

@login_required
def success(request):
    return render(request, 'success.html')
