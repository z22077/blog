from django.shortcuts import render

from article.models import Article, Comment
from article.forms import ArticleForm


def article(request):
    '''
    Render the article page
    '''
    articles = {article:Comment.objects.filter(article=article) for article in Article.objects.all()}
    context = {'articles':articles}
    return render(request, 'article/article.html', context)
# Create your views here.
def articleCreate(request):
    '''
    Create a new article instance
        1. If method is GET, render an empty form
        2. If method is POST,
           * validate the form and display error messages if the form is invalid
           * else, save it to the model and redirect to the article page
    '''
    template = 'article/articleCreate.html'
    if request.method == 'GET':
        return render(request, template, {'articleForm':ArticleForm()})