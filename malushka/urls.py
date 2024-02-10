from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf.urls import url

from accounts.views import (
    login_view,
    logout_view,
)

from click_house.views import (
    click_house_home_view,
)

urlpatterns = [
    path("", views.home, name="malushka-home"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/img/malushka.png')) 
    # path('click_house/',click_house_home_view,name='click_home'),
]
