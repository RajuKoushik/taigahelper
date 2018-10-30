from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.views.generic.base import RedirectView
from api import views
from django.contrib.staticfiles.storage import staticfiles_storage


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^$', RedirectView.as_view(url='home/')),
    url(r'^home/', views.home, name='home'),

]
