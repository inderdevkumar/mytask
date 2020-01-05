"""mytask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from todo.views import mytaskview, addtask, deletetask, edittask,updateview, addtodopage, deletetodopage, edittodopage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mytaskview),
    path('update/', updateview, name='update'),
    path('add/', addtask, name='add'),
    path('addtodo/', addtodopage, name='addtodo'),
    path('deletetodo/', deletetodopage, name='deletetodo'),
    path('edittodo/', edittodopage, name='edittodo'),
    path('delete/<int:todo_id>/', deletetask, name='delete'),
    path('edit/<int:edit_id>/', edittask, name='edit'),


]
