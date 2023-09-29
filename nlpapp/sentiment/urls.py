from django.urls import path
from sentiment import views

app_name = 'sentiment'

urlpatterns = [
    path('', views.index, name='index'),
]