from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Главная страница</h1>')


def about(request):
    return HttpResponse('О сайте')


def contact(request):
    return HttpResponse('Контакты')