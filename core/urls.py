
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home_page_view,name='home-page'),
    path('admin/', admin.site.urls),
]
