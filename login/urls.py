from django.conf.urls import url
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
    url(r'^$', views.signin, name='signin'),
    url(r'^logout', logout, {'next_page': '/login'}, name='logout')
]
