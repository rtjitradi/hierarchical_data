from django.shortcuts import render

from dropboxesque_app.models import DropboxesqueModel


# Create your views here.
def index_view(request):
    return render(request, 'index.html', {'branches': DropboxesqueModel.objects.all()})
