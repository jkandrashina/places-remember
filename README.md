# Приложение Places Remember

## Примечания

- Для работы приложения требуется Python не ниже версии 3.8.

- В модель не было добавлено поле с картой.  
  
  Не хватило времени, чтобы разобраться с геоданными и тем, как выводить и сохранять их.


## Инструкции по настройке приложения

1. Клонируйте репозиторий на свой компьютер:
   ```bash
   git clone git@github.com:jkandrashina/places-remember.git
   ```

2. Откройте командную строку и перейдите в папку places-remember:
   ```bash
   cd places-remember
   ```

3. Создайте в ней виртуальное окружение:

   Linux
   ```bash
   python3 -m venv venv
   ```
   Windows
   ```bash
   python -m venv venv
   ```

4. Активируйте виртуальное окружение, выполнив команду:

   Linux
   ```bash
   source venv/bin/activate
   ```
   Windows
   ```bash
   venv\scripts\activate
   ```

5. Установите необходимые библиотеки, прочитав их список из файла:

   Linux
   ```bash
   (venv) ~$ pip install -r requirements.txt
   ```
   Windows
   ```bash
   (venv)..> python -m pip install -r requirements.txt
   ```

6. Создайте файл .env в корневой папке places-remember и добавьте в него переменные:
   ```bash
   DEBUG=...
   SECRET_KEY='...'
   ```
   SECRET_KEY может быть сгенерирован следующим образом:
   
   ```bash
   from django.core.management.utils import get_random_secret_key
   get_random_secret_key()
   ```

7. Выполните миграции:

   Linux / Windows
   ```bash
   python manage.py migrate
   ```

8. Создайте суперпользователя:

   Linux / Windows
   ```bash
   (venv) ~$ py manage.py createsuperuser
   ```

9. Запустите локальный сервер:

   Linux / Windows
   ```bash
   (venv) ~$ py manage.py runserver
   ```

10. Откройте приложение в браузере, набрав в адресной строке:
   ```bash
   http://127.0.0.1:8000
   ```
   Убедитесь, что приложение работает.

11. Для авторизации пользователей через аккаунты Google / VK необходимо зарегистрировать свое приложение в каждом из сервисов:
   
   Google
   [https://console.developers.google.com/](https://console.developers.google.com/ "Google Developers Console")
   
   VK
   [https://vk.com/editapp?act=create](https://vk.com/editapp?act=create "VK Developers")
   
   
   Информацию о callback urls можно найти здесь:
   [https://django-allauth.readthedocs.io/en/latest/providers.html](https://django-allauth.readthedocs.io/en/latest/providers.html "Oauth Providers")
   
   После регистрации приложения вам будут доступны ключи и id клиента.


12. Перейдите в административный интерфейс и введите данные суперпользователя:
   ```bash
   http://127.0.0.1:8000/admin
   ```

13. В разделе "Сайты" измените сайт example.com следующим образом:
   ```bash
   Доменное имя: http://127.0.0.1:8000
   Отображаемое имя: Places Remember
   ```

14. В разделе "Социальные аккаунты" выберите ссылку "Социальные приложения".

   Здесь необходимо будет добавить 2 приложения: google и vk.
   
   В форме создания приложения выберите имя доступного провайдера.
   
   Введите client_id, secret и key, полученные при регистрации приложения в Google и VK.
   
   В поле Sites выберите http://127.0.0.1:8000.

15. После этого вернитесь на домашнюю страницу сайта и протестируйте авторизацию через каждый из аккаунтов.

16. Если авторизация работает, значит, вы все сделали правильно :)
