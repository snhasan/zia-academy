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

from pages.views import home_view,about_view,contact_view,sendMail
from pages.views import activities_view,activities_details_view,gallery_view,programs_view,programs_details_view,contact_form_view
from myBlogs.views import blog_view
from myBlogs.views import blog_details_view
from blogComment.views import comment_create_view

from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('gallery/', gallery_view, name='gallery'),
    path('programs/', programs_view, name='programs'),
    path('programs-details/<int:pk>/', programs_details_view, name='programs-details_with_pk'),
    path('activities/', activities_view, name='activities'),
    path('activity-details/<int:pk>/', activities_details_view, name='activity-details_with_pk'),
    path('email_send/', sendMail, name='email_send'),
    path('contact_form_view/', contact_form_view, name='contact_form_view'),
    path('contact/', contact_view, name='contact'),
    path('admin/', admin.site.urls),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)