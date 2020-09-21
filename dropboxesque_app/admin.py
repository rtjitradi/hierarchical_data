from django.contrib import admin
from dropboxesque_app.models import DropboxesqueModel
from mptt.admin import DraggableMPTTAdmin


# Register your models here.
admin.site.register(DropboxesqueModel, DraggableMPTTAdmin)
