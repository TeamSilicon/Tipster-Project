from django.conf.urls import url
from . import views

urlpatterns = [
    # for AllGames
    url(r'^$', views.all_games, name='today'),
    url(r'^yesterday/$', views.all_games, name='yesterday'),
    url(r'^tomorrow/$', views.all_games, name='tomorrow'),
    # url(r'game_detail/(?P<pk>[{\w+}* -{\w+}*]+)', views.game_detail, name="game_detail"),
    # url(r'^login/$', views.login, name='login'),
    # # for goalgoal
    # url(r'^goalgoal/today/$', views.goal_Goal, name='goalgoal'),
    # url(r'^goalgoal/yesterday/$', views.goal_Goal, name='goalgoal'),
    # url(r'^goalgoal/tomorrow/$', views.goal_Goal, name='goalgoal'),
    # url(r'^goalgoal/$', views.goal_Goal, name='goalgoal'),
    # # for featured
    # url(r'^featured/today/$', views.featured, name='featured'),
    # url(r'^featured/yesterday/$', views.featured, name='featured'),
    # url(r'^featured/tomorrow/$', views.featured, name='featured'),
    # url(r'^featured/$', views.featured, name='featured'),
    # for jackpot
    # url(r'^jackpot/$', views.jackpot, name='jackpot'),
    # for overtips
    # url(r'^over/today/$', views.over, name='over'),
    # url(r'^over/yesterday/$', views.over, name='over'),
    # url(r'^over/tomorrow/$', views.over, name='over'),
    # url(r'^over/$', views.over, name='over'),
    # # for betslip
    # url(r'^betslip/', views.slip, name='betslip'),
    # for comingsoon
    url(r'^comingsoon/', views.comingsoon, name='comingsoon'),
]
