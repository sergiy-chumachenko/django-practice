from django.contrib import admin
from django.urls import path

from core import views as core_views

urlpatterns = [
    path('home/', core_views.home_page_view, name='homepage'),
    path('signup/', core_views.signup_page_view, name='signup'),
    path('admin/', admin.site.urls),
]
