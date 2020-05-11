"""djangoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from pages.views import home_view,about_view,blog_view,blog_details_views,contact_view,subject_view,sendMail
from myBlogs.views import blog_view
from myBlogs.views import blog_details_view
from blogComment.views import comment_create_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('blog/', blog_view, name='blog'),
    path('email_send/', sendMail, name='email_send'),
    path('subject-details/<curriculum>/<subject>/', subject_view, name='subject-details_with_pk'),
    path('contact/', contact_view, name='contact'),
    path('blog-details/<int:pk>/', blog_details_view, name='blog-details_with_pk'),
    path('blog-details/', comment_create_view, name='comment_create_view'),
    path('admin/', admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)