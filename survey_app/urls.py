from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('survey', views.process_survey),
    path('results', views.results)
]