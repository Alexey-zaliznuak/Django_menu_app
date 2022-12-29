from django.urls import path
from . import views

app_name = "test_menu_app"
urls = [
    'pies/',
        'pies/apple_pie/',
            'pies/apple_pie/opened/',
            'pies/apple_pie/closed/',
        'pies/napaleon/',
            'pies/napaleon/first/',
            'pies/napaleon/second/',
    'ice_cream/',
        'ice_cream/chocolate/',
            'ice_cream/chocolate/white/',
            'ice_cream/chocolate/black/',
        'ice_cream/fruit/',
            'ice_cream/fruit/cold/',
            'ice_cream/fruit/not_cold/',
]

urlpatterns = [
    *[path(url, views.index) for url in urls],
    path('', view=views.index, name='index'), #  name space test
    path('pies/napaleon/', view=views.index, name='napaleon')
]
