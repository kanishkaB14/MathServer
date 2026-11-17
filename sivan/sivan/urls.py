from django.contrib import admin
from django.urls import path
from mysivan import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.calculate_Churn,name='calculate'),
]