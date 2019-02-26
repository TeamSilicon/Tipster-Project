from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.all_games, name='today'),
    url(r'^yesterday/$', views.all_games, name='yesterday'),
    url(r'^tomorrow/$', views.all_games, name='tomorrow'),
    url(r'^featured/$', views.featured, name='featured'),
    url(r'game_details/(?P<pk>[{\w+}* -{\w+}*]+)', views.game_details, name="game_details"),
    url(r'^login/$', views.login, name='login'),
    url(r'^G-G/$', views.Goal_Goal, name='Goal_Goal'),
    # url(r'^wallet/', views.wallet, name='wallet'),
    url(r'^comingsoon/', views.comingsoon, name='comingsoon'),
]
