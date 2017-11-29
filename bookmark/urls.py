from django.conf.urls import url

from bookmark.views import BookMarkDV, BookMarkLV

app_name = 'bookmark'
urlpatterns = [
    url(r'^$', BookMarkLV.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', BookMarkDV.as_view(), name='detail'),
]
