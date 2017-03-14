from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import cbv, fbv

app_name = 'snippets'

urlpatterns = [
    url(r'^snippets/$', cbv.SnippetList.as_view(), name='snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', cbv.SnippetDetail.as_view(), name='snippet_detail'),
    url(r'^users/$', cbv.UserList.as_view(), name='user_list'),
    url(r'^users/(?P<pk>[0-9]+)/$', cbv.UserDetail.as_view(), name='user_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
