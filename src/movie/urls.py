from .views import MovieDetail,MovieList
from django.urls import path

urlpatterns = [
    path('', MovieList.as_view(), name ='movie_list'),
    path('<int:pk>',MovieDetail.as_view(), name='movie_detail'),
]