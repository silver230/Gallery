from django.shortcuts import render
from django.http  import HttpResponse, Http404
import datetime as dt
from django.db import models
from .models import Image

# Create your views here.
# def intro(request):
#     return render(request, 'all-pics/gallery.html')
  

def pics_of_day(request):
    date = dt.date.today()
    photos = Image.get_all()
    return render(request, 'all-pics/gallery.html', {"date": date,"photos":photos})    

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

# def past_days_pics(request,past_date):
#     try:
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()
#         assert False

#     if date == dt.date.today():
#         return redirect(news_today)

#     return render(request, 'all-pics/past-gallery.html',{"date": date,"photos":photos})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get(" image")
        searched_images =  image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message," images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})    


