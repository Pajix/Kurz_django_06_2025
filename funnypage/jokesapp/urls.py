from django.urls import path
from . import views

urlpatterns = [
    path('', views.jokes, name="home-page"),
    path('thank-you', views.thank_you),
    path('all-jokes', views.all_jokes, name="all-jokes-url"),
]