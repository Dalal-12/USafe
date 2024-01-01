from django.urls import path
from . import views

app_name= "main"

urlpatterns= [
    path("" , views.home_view , name= "home_view"),
    path('about/', views.about_view, name="about_view"),
    path('webcam/', views.webcam_view, name="webcam"),
    path("fainted/", views.webcam_result, name="webcam_upload"),
]

