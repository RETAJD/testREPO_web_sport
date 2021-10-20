"""libraryproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from books.views import main, form, books_list, books_details 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"), # dopisane
    path('form/', form, name="form"), # dopisane
    path('books/', books_list, name="book_list"), #dopisane
    path('book/<int:book_id>', books_details, name="books_details")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
