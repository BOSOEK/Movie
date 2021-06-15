from django.contrib import admin

from .models import User, Movie, Opinion
# Register your models here.

class QuestionAdmin(admin.ModelAdmin) :
    search_fields = ['title']

admin.site.register(Movie)
admin.site.register(Opinion)
admin.site.register(User)

