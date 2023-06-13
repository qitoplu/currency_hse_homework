# **Как развернуть проект в локале:**

* Клонировать репозиторий и перейти в директорию с проектом:
> `git clone https://github.com/qitoplu/currency_hse_homework.git`
> `cd currency`
* Cоздать и активировать виртуальное окружение:
> `python3 -m venv env`  
> `source env/bin/activate`
* Установить зависимости:
> `python3 -m pip install --upgrade pip`  
> `pip install -r requirements.txt`
* Выполнить миграции:
> `python3 manage.py migrate`
* Запустить проект:
> `python3 manage.py runserver`
