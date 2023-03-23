from django.shortcuts import render, redirect
import datetime as dt
from django.http  import HttpResponse, Http404

from .models import Article

def index(request):
    date = dt.date.today()
    context = {
        "date": date,
        }
    return render(request, 'index.html', context)

def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    context = {
        "date": date,
        "news": news,
        }
    return render(request, 'news/today-news.html', context)

def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"news/article.html", {"article":article})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_news(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)
    
    news = Article.days_news(date)
    context = {
        "date": date,
        "news": news,
        }

    return render(request, 'news/past-news.html', context)

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'news/search.html', {"message":message})
