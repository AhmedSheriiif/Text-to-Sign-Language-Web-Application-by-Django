from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.home, name='home'),
    path('translate/<str:word>', views.translate_word, name='translate_word'),
]