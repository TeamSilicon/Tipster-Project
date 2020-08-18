from django.urls import path, include
from django.contrib import admin
from home.games_api import GamesViewSet
from rest_framework import routers

from home import views as my_views


router = routers.DefaultRouter()
router.register('games', GamesViewSet, basename='Match')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('pwa.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls))

]

# handler404 = my_views.error_404
handler500 = my_views.error_500
