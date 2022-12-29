from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('test_menu_app.urls', namespace="core")),
    path('admin/', admin.site.urls),
]
