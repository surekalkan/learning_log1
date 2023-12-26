from django.urls import path, include

from . import views

app_name = "users"

# Hangi URL paterni hangi görünüm fonksiyonu ile eşleşecek
urlpatterns = [
    path('', include('django.contrib.auth.urls')),   # Django'nun yerleşik kullanıcı doğrulama sistemine ait URL desenleri
    path('register/', views.register, name='register'),
]
