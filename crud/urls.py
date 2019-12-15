from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('read/<int:task_id>/<str:action>', views.read, name='read'),
    path('update/<int:id>', views.update, name='update'),
    path('update/<str:link>', views.read, name='update'),
]   