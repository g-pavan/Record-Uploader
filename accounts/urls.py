from django.urls import path
from .views import Home, ImageView

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("myapp/", ImageView.as_view(), name="myapp"),
]
