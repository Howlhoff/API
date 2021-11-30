from .views import *
from django.urls import path

urlpatterns=[
    path('',JuegoView.as_view()),
]