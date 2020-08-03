from django.urls import path
from home import views
from django.views.generic import TemplateView

urlpatterns = [
    # for AllGames
    path('', views.all_games, name='today'),
    path('yesterday/', views.all_games, name='yesterday'),
    path('tomorrow/', views.all_games, name='tomorrow'),
    path('login/', views.login, name='login'),

    # path
    path("notify", views.notify, name="notify"),
    # for goalgoal
    path('goalgoal/today/', views.goal_Goal, name='goalgoal'),
    path('goalgoal/yesterday/', views.goal_Goal, name='goalgoal'),
    path('goalgoal/tomorrow/', views.goal_Goal, name='goalgoal'),
    path('goalgoal/', views.goal_Goal, name='goalgoal'),
    # for featured
    path('featured/today/', views.featured, name='featured'),
    path('featured/yesterday/', views.featured, name='featured'),
    path('featured/tomorrow/', views.featured, name='featured'),
    path('featured/', views.featured, name='featured'),
    # for jackpot
    path('jackpot/', views.jackpot, name='jackpot'),
    # for overtips
    path('over/today/', views.over, name='over'),
    path('over/yesterday/', views.over, name='over'),
    path('over/tomorrow/', views.over, name='over'),
    path('over/', views.over, name='over'),
    # for betslip
    path('betslip/', views.slip, name='betslip'),
    # for comingsoon
    path('comingsoon/', views.comingsoon, name='comingsoon'),
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt", content_type='text/plain')),
    # api scope
    path('api/c2b_results', views.c2b_payment_request, name="c2b_results"),
    path('api/validation_callback', views.c2b_validation_callback,
         name='validation_callback'),
    path('api/confirmation_callback', views.c2b_confirmation_callback,
         name='confirmation_callback'),

]
