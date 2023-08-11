from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
  
   path('files_home/',views.file_home, name='file_home'),
   path('files_Submit/',views.file_Submit, name='file_Submit'),
   path('file_upload/',views.file_upload, name='file_upload'),
   path('view_mynotes/',views.view_mynotes, name='view_mynotes'),
   
]