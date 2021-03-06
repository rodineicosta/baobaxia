from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns(
    'tag.views',
    url(r'tags/functional_tag/' + 
        '(?P<tags>[\w\/\-_\ ]*)$', 'check_functional_tags'),    
    url(r'^(?P<repository>\w+)/(?P<mucua>[a-zA-Z0-9\-\[\]]+)/tags/search/' + 
        '(?P<args>[\w\/\-_\ ]*)$', 'search_tags'),
    url(r'^(?P<repository>\w+)/(?P<mucua>[a-zA-Z0-9\-\[\]]+)/tags/' + 
        '(?P<args>[\w\/\-_\ ]+)$', 'search_related_tags'),
    url(r'^(?P<repository>\w+)/(?P<mucua>[a-zA-Z0-9\-\[\]]+)/tags/',
        'mucua_tags'),   
    url(r'^(?P<repository>\w+)/(?P<mucua>[a-zA-Z0-9\-\[\]]+)/tags',
        'mucua_tags'),   
)

urlpatterns = format_suffix_patterns(urlpatterns)
