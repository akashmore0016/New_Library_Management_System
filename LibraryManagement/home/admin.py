from django.contrib import admin
from .models import TextBook, Readers, Proceedings, LibraryBooks

# Register your models here.

admin.site.register(TextBook)
admin.site.register(Readers)
admin.site.register(Proceedings)
admin.site.register(LibraryBooks)