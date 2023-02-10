from django.contrib import admin
from django.urls import path, re_path
from hello import views

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^about', views.about, kwargs={"name":"Maks", "age": 38}),
    re_path(r'^contact', views.contact),
    path('admin/', admin.site.urls),
]
