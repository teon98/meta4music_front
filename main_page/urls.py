from django.urls import path
from . import views 

#main_page/home

app_name='main_page';

urlpatterns=[
    path('',views.home_view, name="home"),
    path('drawing/',views.drawing_view, name="drawing"),
    path('playing/',views.playing_view, name="playing"),

]