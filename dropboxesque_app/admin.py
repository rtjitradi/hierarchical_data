from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from dropboxesque_app.models import DropboxesqueModel


# Register your models here.
admin.site.register(DropboxesqueModel, DraggableMPTTAdmin)
