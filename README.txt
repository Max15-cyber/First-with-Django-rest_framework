C:/Users/User/AppData/Local/Programs/Python/Python38-32/python.exe -m venv venv # Создание venv

python -m pip install --upgrade pip
pip install django djangorestframework
django-admin startproject blog_project
cd blog_project
python manage.py startapp blog
python manage.py runserver
python manage.py migrate

# При изменении бд
python manage.py makemigrations
python manage.py migrate
# Регистрация админа
python manage.py createsuperuser

Maxim
max@mail.com
123456

pip install pillow

venv\Scripts\activate

# Подключаем postgres
pip install psycopg2

# models
python manage.py shell # shell
from blog.models import Post

POST

Post(title = 'Title2', content = 'Post2')
u2 = _
u2.save()

GET

u1.pk
u1.id

# Посмотреть SQL-запрос

from django.db import connection
connection.queries
Post.objects.all()
Post.objects.all()[0]
Post.objects.all()[0].title

Post.objects.filter(pk = 10) # Пустой список

# >=
Post.objects.filter(pk__gte = 7)

# <= 
Post.objects.filter(pk__lte = 7)

# <
Post.objects.filter(pk__lt = 7)

# >
Post.objects.filter(pk__gt = 7)

# исключение поста
Post.objects.exclude(title = 'Title1')

# Получить уникальную запись
Post.objects.get(pk = 9)
Post.objects.get(pk = 10) # Остутствует / несколько => ошибка

# Сортировка
Post.objects.all().order_by('-id')

# UPDATE
post_9 = Post.objects.get(pk = 9)
post_9.title = 'Title_9'
post_9.title
post_9.save()

# DELETE
Post.objects.get(pk = 7).delete()

# Выход
exit()