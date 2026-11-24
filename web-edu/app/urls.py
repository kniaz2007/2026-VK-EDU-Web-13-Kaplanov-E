"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from questions import views
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('hot', views.hot, name = "hot"),
    path('add_question',views.add, name = "add_question"),
    path('registration',views.reg, name = "reg"),
    path('login', views.login, name = "login"),
    path('one_question/<int:question_id>/', views.one_question, name = "one_question"),
    path('setings', views.setings, name = "setings"),
    path('tag/<tag_name>/', views.tag, name = "tag"),
    
]

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()

