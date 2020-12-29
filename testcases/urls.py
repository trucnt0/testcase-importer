from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:testcase_id>/', views.get, name='get'),    
    path('delete/<int:testcase_id>', views.delete, name='delete'),    
    path('save', views.save, name='save')
]
