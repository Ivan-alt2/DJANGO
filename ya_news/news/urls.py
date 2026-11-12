from django.contrib import admin
from django.urls import include, path

from news.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/logout/', logout_view, name='logout'),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('news.urls')),
]
