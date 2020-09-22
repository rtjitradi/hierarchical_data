from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate

from dropboxesque_app.models import DropboxesqueModel
from dropboxesque_app.forms import DropboxesqueForm, LoginForm


# Create your views here.
# username: reggy / password: asdf
def index_view(request):
    return render(request, 'index.html', {'branches': DropboxesqueModel.objects.all()})


def create_view(request):
    if request.method == 'POST':
        form = DropboxesqueForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_dropboxesque = DropboxesqueModel.objects.create(
                name=data['name'],
                parent=data['parent']
            )
            if new_dropboxesque:
                return HttpResponseRedirect(reverse('homepage'))

    form = DropboxesqueForm()
    return render(request, 'genericform.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data.get('username'),
                password=data.get('password')
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, 'genericform.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
