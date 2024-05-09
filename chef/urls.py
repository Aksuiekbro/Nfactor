from django.urls import path

from . import views
app_name = "chef"
urlpatterns = [
    path("search/<str:user_input>", views.index, name="index"),
    path("", views.home, name="home"),
]