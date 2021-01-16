from django.shortcuts import render,redirect
from .models import Movie,Screenshot,Category,Movie_file
from django.http import HttpResponse
from datetime import datetime




def index(request):
    movies = Movie.objects.all()[:10]
    count = None
    return render(request,'home.html',{'movies':movies,'count':count})


def movie_info(request,id):
    movie            = Movie.objects.get(id=id)
    movie_categories = Category.objects.filter(Movie_id=id)
    screenshots      = Screenshot.objects.filter(Movie_id=id)
    qualities        = Movie_file.objects.filter(Movie_id=id)
    category = ''
    for i,cat in enumerate(movie_categories):
        if i==0:
            category = cat.Name
        else:
            category = category + '|' + cat.Name
  
    context = {'movie':movie,'categories':category,'screenshots':screenshots,'qualities':qualities}
    return render(request,'movie_info.html',context)

def play_movie(request,id,quality_type):
    movie = Movie_file.objects.get(Movie_id=id,Quality_type=quality_type)
    return render(request,'play_movie.html',{'movie':movie})


def download_movie(request,id,quality_type):
    movie = Movie_file.objects.get(Movie_id=id,Quality_type=quality_type)
    file_name = movie.File.name
    path = f'media//{movie.File}'
    movie_file = open(path,'rb')
    http_response = HttpResponse(movie_file,content_type='application/MP4')
    http_response['Content-Disposition'] = f'attachment; filename={file_name}'
    return http_response


def category_by(request,category_name):
    movies = Category.objects.filter(Name=category_name)
    cat_by_movies = []
    for movie in movies:
        cat_by_movies.append(movie.Movie)

    return render(request,'home.html',{'movies':cat_by_movies})

    


def latest_movies(request):
    current_year = f'{datetime.now().year}-1-1'
    movies = Movie.objects.filter(Released_date__gte=current_year)
    return render(request,'home.html',{'movies':movies})


# def find_movie(request):
#     movie_name = request.GET.get('search')
#     movie = Movie_info.objects.get(M_name=movie_name)
#     return render(request,'searchmovie.html',{'i':movie})




# def nextpage(request,no):
#     movies = Movie_info.objects.all()[(no-1)*4:(no)*4]
#     return render(request,'index.html',{'movie_info':movies})



