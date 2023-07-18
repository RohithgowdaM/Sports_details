from django.urls import path
from . import views

urlpatterns = [
    path('',views.list,name='list'),
    path('homepage',views.homepage,name='homepage'),
    path('student',views.student,name='student'),
]
