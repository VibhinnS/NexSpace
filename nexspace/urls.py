from django.contrib import admin
from django.urls import path, include
from .views import landing_page, question_list, sign_in, sign_out
# from questions import views  # Remove this line if it's not needed

urlpatterns = [
    path('', landing_page),
    path('questions/', question_list, name="questions"),
    path('admin/', admin.site.urls),
    path('sign-in/', sign_in, name="sign_in"),
    path('sign-out/', sign_out, name="sign_out"),
    path("accounts/", include("allauth.urls")),
    # path("", include("users.urls")),  # Change "/" to "" if this is intended for root URL pattern
    path("__reload__/", include("django_browser_reload.urls")),
]
