from django.conf.urls import url, include
from django.contrib import admin

from home import views as my_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('home.urls')),
    url('', include('pwa.urls')),

]

# handler404 = my_views.error_404
handler500 = my_views.error_500
