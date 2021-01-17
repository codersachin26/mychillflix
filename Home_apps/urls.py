from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns =[
  
    path('',views.index,name='home page'),
    path('movie_info/<int:id>',views.movie_info,name='movie_info'),
    path('play_movie/<int:id>/<str:quality_type>',views.play_movie,name='play_movie'),
    path('download_movie/<int:id>/<str:quality_type>',views.download_movie,name='download_movie'),
    path('category_by/<str:category_name>',views.category_by,name='category_by'),
    path('latest_movies',views.latest_movies,name='latest_movies'),
    path('find_movie',views.find_movie,name='find_movies'),
  

]
