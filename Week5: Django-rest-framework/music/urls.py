from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test/$', views.Testing.as_view()),
    url(r'^art/$', views.ArtistDetail.as_view()),
    url(r'^track_detail/$', views.TrackDetail.as_view()),
]
