from django.conf.urls import url
from django.urls import path
from home import views
from django.views.generic import TemplateView

urlpatterns = [
    # for AllGames
    url(r'^$', views.all_games, name='today'),
    url(r'^yesterday/$', views.all_games, name='yesterday'),
    url(r'^tomorrow/$', views.all_games, name='tomorrow'),
    url(r'^login/$', views.login, name='login'),

    # path
    path("notify", views.notify, name="notify"),
    # for goalgoal
    url(r'^goalgoal/today/$', views.goal_Goal, name='goalgoal'),
    url(r'^goalgoal/yesterday/$', views.goal_Goal, name='goalgoal'),
    url(r'^goalgoal/tomorrow/$', views.goal_Goal, name='goalgoal'),
    url(r'^goalgoal/$', views.goal_Goal, name='goalgoal'),
    # for featured
    url(r'^featured/today/$', views.featured, name='featured'),
    url(r'^featured/yesterday/$', views.featured, name='featured'),
    url(r'^featured/tomorrow/$', views.featured, name='featured'),
    url(r'^featured/$', views.featured, name='featured'),
    # for jackpot
    url(r'^jackpot/$', views.jackpot, name='jackpot'),
    # for overtips
    url(r'^over/today/$', views.over, name='over'),
    url(r'^over/yesterday/$', views.over, name='over'),
    url(r'^over/tomorrow/$', views.over, name='over'),
    url(r'^over/$', views.over, name='over'),
    # for betslip
    url(r'^betslip/', views.slip, name='betslip'),
    # for comingsoon
    url(r'^comingsoon/', views.comingsoon, name='comingsoon'),
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt", content_type='text/plain')),
    # api scope
    path('api/c2b_results', views.c2b_payment_request, name="c2b_results"),
    path('api/validation_callback', views.c2b_validation_callback,
         name='validation_callback'),
    path('api/confirmation_callback', views.c2b_confirmation_callback,
         name='confirmation_callback'),

]
