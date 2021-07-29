from django.shortcuts import render
from pprint import pprint

from articles.models import Article, TagLink, Tag


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-taglink__is_main'

    articles = Article.objects.order_by(ordering).prefetch_related('tag').values('id', 'title', 'image', 'text',
                                                                                     'tag__name',
                                                                                     'taglink__is_main')

    object_list = []
    articles_hash = []
    for article in articles:
        if article['id'] not in articles_hash:
            articles_hash.append(article['id'])
            art_dict = {}
            art_dict['id'] = article['id']
            art_dict['title'] = article['title']
            art_dict['image'] = article['image']
            art_dict['text'] = article['text']
            art_dict['scopes'] = [{'tag': article['tag__name'], 'is_main': article['taglink__is_main']}]
            object_list.append(art_dict)
        else:
            for obj in object_list:
                if obj['id'] == article['id']:
                    obj['scopes'].append({'tag': article['tag__name'], 'is_main': article['taglink__is_main']})

    context = {
        'object_list': object_list
    }



    return render(request, template, context)
