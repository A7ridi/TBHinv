from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item_entry', views.item_entry, name='item_entry'),
    path('item_list', views.item_list, name='item_list'),
    path('item_list/<int:id>', views.list_edit, name='list_edit'),
    path('item_list/<int:id>/delete', views.item_delete, name='item_delete'),
    path('storagehistory_list/', views.storagehistory_list, name='storagehistory_list'),


]