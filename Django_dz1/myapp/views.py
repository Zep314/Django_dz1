from django.shortcuts import render

# Create your views here.
import logging
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    html = """

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>
        Мой сайт - Главная
    </title>
</head>
<body>
<div>
    <header>
        <nav>
            <div style="display: flex; gap: 20px;">
                <a href="/">Главная</a>
                <a href="/about">О нас</a>
            </div>
        </nav>
        <h1>
            Главная страница моего сайта
        </h1>
    </header>
    <main>
        <p>
            Центральная часть главной страницы моего сайта
        </p>    
    </main>

    <footer>
        <div>
            <p>
            Все права защищены &copy;
            </p>
        </div>
    </footer>
</div>
</body>
</html>

    """
    logger.info('Index page accessed')
    return HttpResponse(html)


def about(request):
    html = """

    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>
            Мой сайт - О нас
        </title>
    </head>
    <body>
    <div>
        <header>
            <nav>
                <div style="display: flex; gap: 20px;">
                    <a href="/">Главная</a>
                    <a href="/about">О нас</a>
                </div>
            </nav>
            <h1>
                Страница "О нас" моего сайта
            </h1>
        </header>
        <main>
            <p>
                Центральная часть страницы "О нас" моего сайта
            </p>    
        </main>

        <footer>
            <div>
                <p>
                Все права защищены &copy;
                </p>
            </div>
        </footer>
    </div>
    </body>
    </html>

        """

    logger.info('About page accessed')
    return HttpResponse(html)
