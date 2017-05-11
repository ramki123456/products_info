"""TestPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from myapp import views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^welcome$',views.show_welcome),
    url(r'^$',views.load_login),
    url(r'^get_rec/', views.get_my_record),
    url(r'^login/', views.check_login),
    url(r'^load_add_stock_page', views.load_add_stock_page),
    url(r'^save_data_to_db/', views.add_data_to_db),
]