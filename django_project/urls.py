from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name= 'home'),
    path('index/', views.homeindex, name= 'homeindex'),
    path('index1/', views.home1, name= 'home1'),
    path('index2/', views.home2, name= 'home2'),
    path('index3/', views.home3, name= 'home3'),
    path('index4/', views.home4, name= 'home4'),
    path('index5/', views.home5, name= 'home5'),
    path('index6/', views.home6, name= 'home6'),
    path('index7/', views.home7, name= 'home7'),
    path('index8/', views.home8, name= 'home8'),
    path('age_chart/', views.age_chart, name='age_chart'),
    path('sex_chart/', views.sex_chart, name='sex_chart'),
    path('perform_ocr', views.perform_ocr, name='perform_ocr'),
    path('admin/', admin.site.urls),    
]
