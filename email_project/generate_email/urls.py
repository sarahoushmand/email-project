from django.urls import path
from . import views
app_name = 'generate_email'
urlpatterns = [
    path('', views.home, name='home'),
    path('generate', views.generate, name='generate'),
    path('email/', views.email, name='email'),
    path('email/<int:pk>', views.getMessage, name='message'),
]
