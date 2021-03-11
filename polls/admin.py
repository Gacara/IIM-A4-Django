from django.contrib import admin

from .models import Question, Contact

admin.site.register(Question)
admin.site.register(Contact)