from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.pics_of_day,name='pics'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_pics,name = 'pastPics'),
    url(r'^search/', views.search_results, name='search_results'),
    
]