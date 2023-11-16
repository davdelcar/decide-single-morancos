from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.BaseView.as_view(), name='base'),
     path('admin/', admin.site.urls),

]
