from django.urls import path
from cal_app import views

urlpatterns = [
    path('',views.index,name='home'),
    path('delete/<int:id>',views.delete_food,name='delete'),
    path('delete_all/',views.delete_all,name='delete_all')
]