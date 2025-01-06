from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('item/', views.item, name='item'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    # adding items
    path('add/', views.CreateItem.as_view(), name='create_item'),
    #editing Items
    path('update/<pk>/', views.UpdateItem.as_view(), name='update_item'),
    # deleting items
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]