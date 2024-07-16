from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('trainer/', views.trainer, name='trainer'),
    path('blog/', views.blog, name='blog'),
    path('why/', views.why, name='why'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register')
]
