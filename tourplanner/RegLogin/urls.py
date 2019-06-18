from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="front-page"),
    path("1/", views.register_guide, name="register_guide"),
    path("2/", views.register_user, name="register_user"),
    path("guide/", views.guide_registration_data, name="guide_registration_data"),
    path("user/", views.user_registration_data, name="user_registration_data")
]