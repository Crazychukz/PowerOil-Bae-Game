from django.conf.urls import url, include
from . import views

from Baegame.views import  HomeViews

urlpatterns = [
    url(r'^$', HomeViews.as_view(), name='index'),
]