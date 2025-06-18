from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('experience/', views.experience, name='experience'),
    # path('contact_form/', views.contact_form, name='contact_form'),
]