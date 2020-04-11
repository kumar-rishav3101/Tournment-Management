"""Openended URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Management import views

urlpatterns = [
    url(r'^Delete_Tournment/',views.Delete_Tournment,name='Delete_Tournment'),
    url(r'^Delete_Team/(?P<pk>\d+)/$',views.Delete_Team.as_view(),name='Delete_Teams'),
    url(r'^Delete_Players/(?P<pk>\d+)/$',views.Delete_Players.as_view(),name='Delete_Player'),
    url(r'^update/(?P<pk>\d+)/$',views.PlayerUpdate.as_view(),name='Update'),
    url(r'^AddTeam/',views.form_Team,name='Add_Team'),
    url(r'^AddPlayers/',views.form_Player,name='Add_Players'),
    url(r'^AddTournment/',views.TournmentCreateView.as_view(),name='Add_Tournment'),
    url(r'^Players/(?P<pk>\d+)/$',views.Players.as_view(),name='Players'),
    url(r'^Team/(?P<pk>\d+)/$',views.Team.as_view(),name='Team'),
    url(r'^Delete_T/(?P<pk>\d+)/$',views.Delete_T,name='Delete_T'),
    url(r'^Delete_TM/(?P<pk>\d+)/$',views.Delete_TM,name='Delete_TM'),
    url(r'^Delete_P/(?P<pk>\d+)/$',views.Delete_P,name='Delete_P'),
    url(r'^Tournment/',views.Tournmentt,name='Tournment'),
    path('admin/', admin.site.urls),
]
