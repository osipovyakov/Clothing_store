# Проект Мой магазин

## Описание проекта
Интернет-магазин в котором представлен каталог продуктов и корзина для покупок с помощью сессий.
Был реализован пользовательский контекстный процессор, чтобы сделать корзину доступной для шаблонов и создавать форму для размещения заказов.

## Инструкция по запуску проекта локально

1. Клонировать репозиторий

    - с помощью SSH
    ```bash
    git clone git@github.com:osipovyakov/test_shop.git
    ```
    - с помощью HTTPS
    ```bash
    git clone https://github.com/osipovyakov/test_shop.git
    ```
2. Cоздать и активировать виртуальное окружение, установить зависимости

    - установить виртуальное окружение
   ```bash
   python3.9 -m venv venv
   ```
  - Установить зависимости из файла requirements.txt
  ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
  ```
3. Выполнить миграции и запустить проект
  - Выполнить миграции:
  ```bash
    python manage.py makemigrations
    python manage.py migrate
  ```

  - В папке с файлом manage.py выполнить команду:
  ```bash
    python manage.py runserver
  ```

---

**Автор**

Осипов Яков
