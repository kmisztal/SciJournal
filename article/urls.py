
try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'article.views.year'),
                       url(r'^(?P<publication_id>\d+)/$', 'article.views.id'),
                       url(r'^year/(?P<year>\d+)/$', 'article.views.year'),
                       url(r'^tag/(?P<keyword>.+)/$', 'article.views.keyword'),
                       url(r'^list/(?P<list>.+)/$', 'article.views.list'),
                       url(r'^unapi/$', 'article.views.unapi'),
                       url(r'^(?P<name>.+)/$', 'article.views.person'),
                       )
