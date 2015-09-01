from . import views
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^register/$', views.register, name='register'),
    url(r'^confirm/(?P<activation_key>\w+)/', views.register_confirm),
    
]