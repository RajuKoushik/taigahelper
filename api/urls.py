from django.conf.urls import url
from django.views.generic.base import RedirectView
from api import views

app_name = 'blog'

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [


]
