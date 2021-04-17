from django.urls import path
from django.conf.urls import url
from . import views

app_name = "main"


urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details),
    url(r'^updateItem/(?P<id>\w{0,50})/$', views.updateItem),
    url(r'^deleteItem/(?P<id>\w{0,50})/$', views.deleteItem),
    path("addItem", views.addItem, name="addItem"),
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_view, name="logout"),
]
