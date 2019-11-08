from django.urls import path
from myCrud_App import views
urlpatterns = [
    path('', views.index,name='index'),
    path('create/',views.create,name='create'),
    path('add_book',views.add_book,name='add_book'),
    path('edit/<id>',views.edit,name='edit'),
    path('delete/<id>',views.delete,name='delete'),
    path('update/<id>',views.update,name='update')
]