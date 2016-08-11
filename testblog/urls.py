from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.posts, name='posts'),
    url(r'^/cabinet', views.profile),
    url(r'^/add', views.add),
    url(r'^/article/([0-9]+)', views.article),
    url(r'^/edit/([0-9]+)', views.edit),
    url(r'^/delete/([0-9]+)', views.delete_post),
]
