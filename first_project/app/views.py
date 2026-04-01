from django.http import HttpResponse


def home_view(request):
    """Главная страница."""
    return HttpResponse(
        "<h1>Мой первый Django проект!</h1>"
        "<p>Домашнее задание выполнено успешно.</p>"
        "<p>Автор: Anka</p>"
    )