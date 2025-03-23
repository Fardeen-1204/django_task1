"""
URL configuration for EmpDetails project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Emp_Info.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="emp_details"),
    path('create_emp_details/', create_emp_details,name="emp_details_form"),
    path('emp_delete/<pk>',delete_emp_details,name='emp_delete'),
    path('update_emp_page/<pk>',update_emp_page,name="page_update"),
    path('emp_update/<int:pk>/',update_emp, name='emp_update'),
    path('emp_card/<int:pk>/',emp_card,name='emp_card'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)