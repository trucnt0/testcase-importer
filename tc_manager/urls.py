from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:testcase_id>/', views.get, name='get'),    
    path('save', views.save, name='save')
]
