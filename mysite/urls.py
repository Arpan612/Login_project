from django.contrib import admin

from django.conf.urls import url, include

from django.contrib.auth import views
from app.views import home
from app.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
    url(r'^$', home, name='home'),
]
#url(r'^accounts/login$', 'django.contrib.auth.views.login'),
