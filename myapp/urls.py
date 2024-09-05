from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('loginuser', views.loginuser, name="loginuser"),
    path('logoutuser', views.logoutuser, name="logoutuser"),
    path('about', views.about, name="about"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('imagedetails/<int:id>', views.showfullimage, name="showfullimage"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
