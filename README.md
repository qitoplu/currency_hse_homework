# **Как развернуть проект в локале:**
* Клонировать репозиторий и перейти в директорию с проектом:
> `git clone https://github.com/qitoplu/currency_hse_homework.git`  
> `cd currency`
* Cоздать и активировать виртуальное окружение:
> `python -m venv env`  
> `. venv/Scripts/activate`
* Установить зависимости:
> `python -m pip install --upgrade pip`  
> `pip install -r requirements.txt`
* Выполнить миграции:
> `python manage.py migrate`
* Запустить проект:
> `python manage.py runserver`
