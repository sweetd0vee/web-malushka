from django.urls import path
from . import views


from click_house.views import (
    click_house_home_view,
    access_denied,
)

urlpatterns = [
    path("", click_house_home_view, name="click_home"),
    #path("test/", click_house_home_test_view, name="click_home_test"),
    path("access_denied/", access_denied, name="access_denied"),
]
