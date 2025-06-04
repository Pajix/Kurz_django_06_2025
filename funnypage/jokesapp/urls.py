from django.urls import path
from . import views

urlpatterns = [
    path('', views.jokes),
    path('thank-you', views.thank_you)
]