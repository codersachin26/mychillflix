from django.db import models

# Create your models here.

## store movie meta data
class Movie(models.Model):
    Name          = models.CharField(max_length=50)
    Story         = models.CharField(max_length=500)
    Time_lenght   = models.DurationField()
    Makers        = models.CharField(max_length=50)
    Released_date = models.DateField()
    Languages     = models.CharField(max_length=50)
    Poster        = models.ImageField(upload_to='movie_poster/')
    Big_Poster    = models.ImageField(upload_to='movie_poster/',default='None')

    def __str__(self):
        return self.Name


## store video file of movie
class Movie_file(models.Model):
    Movie        = models.ForeignKey('Movie',on_delete=models.CASCADE)
    Quality_type = models.CharField(max_length=20)
    File         = models.FileField(upload_to='movie_file/')

    def __str__(self):
        return self.Movie.Name +'_' + self.Quality_type

## store movie category
class Category(models.Model):
    Movie = models.ForeignKey('Movie',on_delete=models.CASCADE)
    Name  = models.CharField(max_length=20)

    def __str__(self):
        return self.Movie.Name+'_'+ self.Name 

## store movie screenshot
class Screenshot(models.Model):
    Movie = models.ForeignKey('Movie',on_delete=models.CASCADE)
    File = models.ImageField(upload_to='movie_screenshot/')

    def __str__(self):
        return self.Movie.Name+'_'+self.File.name
