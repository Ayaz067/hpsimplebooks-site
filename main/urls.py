from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('our_services/', views.our_services, name='our_services'),
    path('why_choose_us/', views.why_choose_us, name='why_choose_us'),
    path('contact/', views.contact, name='contact'),
    path('new_client_questionnaire/', views.new_client_questionnaire, name='new_client_questionnaire'),
]