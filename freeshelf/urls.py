"""freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from app import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_views.home, name='home')
    path('books/add/', app_views.add_book, name='add_book'),
    path('books/<int:pk>/', app_views.show_book, name='show_book'),
    path('books/<int:pk>/edit/', app_views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', app_views.delete_book, name='delete_book'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
