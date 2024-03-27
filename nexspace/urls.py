from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing_page, name="landing_page"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
    path('questions/', views.question_list, name="questions"),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
