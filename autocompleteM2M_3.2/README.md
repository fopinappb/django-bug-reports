sample app for https://code.djangoproject.com/ticket/33489

Reproduce steps:

```
cd testapp
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```


