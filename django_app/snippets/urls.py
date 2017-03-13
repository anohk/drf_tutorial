from django.conf.urls import url
from snippets import views

app_name = 'snippets'

urlpatterns = [
    url(r'^snippets/$', views.snippet_list, name='snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detial, name='snippet_detail'),
]