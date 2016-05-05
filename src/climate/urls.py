from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'pull', views.pull, name='pull'),
    url(r'^$', views.index, name='index'),
]

