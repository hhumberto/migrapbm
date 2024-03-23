from django.contrib import admin
from django.urls import path
from pbmconnector import views, migradata



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('datatofhir/', migradata.datatofhir, name='datatofhir')
]