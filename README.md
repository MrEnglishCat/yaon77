# ydhr77

## 🛠️ развертывание

### 1. Клонировать репозиторий:
```bash
git clone https://github.com/MrEnglishCat/yaon77.git 

cd yaon77

```

### 1.1 Создать .env и заполнить его
```aiignore
      # находясь в каталоге с проектом создать файл .env
      touch .env  # создание
      nano .env  # открыть для редактирования
      
      скопировать в файл 
      
            SQLALCHEMY_TRACK_MODIFICATIONS=False
            POSTGRES_USER=postgres
            POSTGRES_PASSWORD=postgres
            POSTGRES_DB=flask_db
            SQLALCHEMY_DATABASE_URI="postgresql://postgres:postgres@db/flask_db"
            
      сохранить файл 
      
```

### 2. Дальше нужно установить на систему докер
https://docs.docker.com/engine/install/

### 3. После перехода в каталог проекта ```cd yaon77``` 
нужно запустить сборку и запуск всех контейнеров через docker-compose.yml


```
docker-compose up --build
```
## Ниже что связано с PgAdmin - нужно только для просмотра базы данных. Для работы самого приложения он не нужен. 
После запуска контейнеров можно сразу переходить к пункту 6. На страницу Flask app.

### 4. PgAdmin работает на порту 8080 

http://localhost:8080

Заходим в него. 
```aiignore
username = admin@admin.com
password = admin
```
### 5. Далее нужно создать сервер через PgAdmin (если есть необходимость посмотреть БД через него). 
    Далее по цифрам на скриншоте после авторизации на странице http://localhost:8080:
    1. Правая кнопка мыши на пункте Servers
    2. Пункт Register -> Server... - выбрать этот пункт Server
    3. В появившемся окне. Вкладка General  
        указать имя сервера: test (можно другое)
    4. Перейти во вкладку Connection
        заполнить поля со  скриншота:
            НАЗВАНИЕ                ЗНАЧЕНИЕ
            --------------------------------
            Host name/address:      db
            Port:                   5432
            Maintenance database:   postgres
            Username:               postgres
            Password:               postgres
    Далее нажимаем кнопку Save для сохранения данных. 

![img_1.png](img_1.png)

[//]: # (### 6. СЕЙЧАС ЭТО НЕ НУЖНО, миграции проверяются при создании докер контейнера. Нужно создать нужную базу данных &#40;нумерация по цифрам на скриншоте&#41;)

[//]: # (    1. Нажать правой кнопкой мыши)

[//]: # (    2. В контекстном меню выбрать Create -> Database... нажать)

[//]: # (    3. Ввести имя базыданных: flask_db)

[//]: # (    Далее нажать кнопку Save &#40;Сохранить&#41;)

[//]: # ()
[//]: # (![img_3.png]&#40;img_3.png&#41;)
    
[//]: # (### 7. После этого нужно остановить контейнер и запустить его заново)

[//]: # ()
[//]: # (```aiignore)

[//]: # (    docker-compose down # остановка контейнера или Ctrl + C)

[//]: # (    )
[//]: # (    docker-compose up --build  # повторная сборка и запуск)

[//]: # (    )
[//]: # (    )
[//]: # (```)

### 6. Адреса страниц:
    http://localhost:8080  - PgAdmin
    http://localhost:8081  - web app Flask