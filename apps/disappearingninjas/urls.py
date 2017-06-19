from django.conf.urls import url
from . import views
app_name = 'disappearingninjas'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ninjas$', views.ninjas, name='ninjas'),
    url(r'^ninjas/(?P<color>.+)$', views.thisninja, name='thisninja')
]