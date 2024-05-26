from django.urls import path

app_name = 'denial_posting'

from . import views
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload, name='upload'),
    path('review/', views.review, name='review'),
]