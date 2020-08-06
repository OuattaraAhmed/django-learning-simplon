from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    re_path(r'^supprimer/(?P<id>[0-9]+)', views.supprimer, name='supprimer'),

]
