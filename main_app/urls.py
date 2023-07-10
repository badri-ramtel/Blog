from django.urls import path
from main_app import views

urlpatterns = [
    path('home/', views.home, name='mainapp-home'),
    path('add/', views.add, name='mainapp-add'),
    path('edit/<int:id>', views.edit, name='mainapp-edit'),
    path('delete/<int:id>', views.delete, name='mainapp-delete'),
    path('blogsview/<int:id>', views.blogsview, name='mainapp-blogsview'),
]
