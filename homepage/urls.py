from django.urls import path
from . import views

urlpatterns = [
  
    path('', views.homepage, name='homepage'),
    path('add', views.addtodo, name='add'),
    path('complete/<todo_id>', views.completetodo, name='complete'),
    path('detelecomplete', views.deletecomplete, name='deletecomplete'),
    path('as', views.saveurl, name='saveurl'),
    path('as', views.saveurl, name='posturl')
    

]
