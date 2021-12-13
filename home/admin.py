from django.contrib import admin

from home.models import contact
from home.models import upload_book


# Register your models here.
admin.site.register(contact)
admin.site.register(upload_book)