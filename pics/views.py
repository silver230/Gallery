from django.shortcuts import render,redirect
from django.http  import Http404
import datetime as dt

# Create your views here.
# def intro(request):
#     return render(request, 'all-pics/gallery.html')

def pics_of_day(request):
    date = dt.date.today()
    
    return render(request, 'all-pics/gallery.html', {"date": date})    

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_pics(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    return render(request, 'all-pics/past-gallery.html',{"date": date})