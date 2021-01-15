from django.contrib import admin
from .models import Movie_file,Movie,Screenshot,UserComments,Category


# Register your models here.
admin.site.register(Movie)
admin.site.register(Movie_file)
admin.site.register(Screenshot)
admin.site.register(UserComments)
admin.site.register(Category)



