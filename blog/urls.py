from django.conf.urls import url
# importa o conteúdo de views
from . import views

urlpatterns = [
    #adiciona o caminho raiz para views.post_list
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
