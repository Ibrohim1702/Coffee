from django.urls import path

from sayt.views import index, about, gallery, contact, services

urlpatterns = [
    path("", index, name="home"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    path("gallery/", gallery, name="gallery"),
    path("services/", services, name="services"),

]
