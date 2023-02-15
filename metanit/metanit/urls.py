from django.contrib import admin

from django.urls import path, re_path

from hello import views

urlpatterns = [
    path('index', views.index),
    # re_path позволяет задать адреса URL с помощью регулярных выражений.
    # view: функция-представление, которое обрабатывает запрос
    # kwargs: дополнительные аргументы, которые передаются в функцию-представление
    re_path(r'^about', views.about, kwargs={"name":"Maks", "age": 38}),
    re_path(r'^contact', views.contact),
    path('admin/', admin.site.urls),
    # Общие маршруты должны идти в конце
    # name: название маршрута
    path('', views.index, name='home'),
]
