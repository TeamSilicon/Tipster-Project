from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='today'),
    url(r'^yesterday/$', views.home, name='yesterday'),
    url(r'^tomorrow/$', views.home, name='tomorrow'),
    url(r'^featured/$', views.featured, name='featured'),
    url(r'game_details/(?P<pk>[{\w+}* -{\w+}*]+)', views.game_details, name="game_details"),
    url(r'^login/$', views.login, name='login'),
    # url(r'^wallet/', views.wallet, name='wallet'),
    url(r'^comingsoon/', views.comingsoon, name='comingsoon'),
]
