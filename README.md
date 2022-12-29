# Django tree-like menu
### Describe
Django app for creating tree-like beautiful ~~only with bootstrap~~ menus
### Technology
Python 3.11
Django 4.1.4
### Start in dev mode
- Install and set environment
- Install dependencies from requirements.txt
```
pip install -r requirements.txt
``` 
- In the folder with manage.py run next command:
```
python manage.py runserver
```
### How test_menu_app work
There are urls in urls.py

```
urls = [
'pies/',
'pies/apple_pie/',
...            
]

urlpatterns = [
    *[path(url, views.index) for url in urls],
    path('', view=views.index, name='index'), #  name space test
    path('pies/napaleon/', view=views.index, name='napaleon')
]
```

Urls have tree-like structure and was dublicate in Resource model.

### Important!
if you want to use namespaces instead
of regular urls like for example in the
last 2 lines urls.py then do not forget
to specify this when creating a Resource
in the admin panel.