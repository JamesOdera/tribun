from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.news_today, name='newsToday'),
    path('archives/(\d{4}-\d{2}-\d{2})/', views.past_days_news, name='pastNews'),
    path('search/', views.search_results, name='search_results'),
    path('article/<int:article_id>/', views.article, name ='article')
]
