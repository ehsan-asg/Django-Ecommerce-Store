from django.urls import path
from . import views
app_name = "website"
from django.views.decorators.cache import cache_page


urlpatterns = [
    path("",(cache_page(60 * 15))(views.IndexView.as_view()),name="index"),
    path("contact/",(cache_page(60 * 30))(views.ContactView.as_view()),name="contact"),
    path("about/",(cache_page(60 * 30))(views.AboutView.as_view()),name="about"),
    path("submit/ticket/", (cache_page(60 * 10))(views.SendContactView.as_view()), name="submit-ticket"),
    path("newsletter/", (cache_page(60 * 10))(views.NewsletterView.as_view()), name="newsletter"),
]

