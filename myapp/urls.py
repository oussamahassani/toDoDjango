from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.project, name='projects'),
    path('projects/<int:id>', views.projectdetail, name='projectdetail'),
    path('projects/delete/<int:id>', views.projectdelete, name='projectdelete'),
    path('projects/delete/confirm/<int:id>', views.projectdeleteconfirm, name='projectdeleteconfirm'),
    path('tasks/', views.tasks, name='tasks'),
    path('createtask/', views.createtask, name='create_task'),
    path('tasks/delete/<int:id>', views.deletetask, name='deletetask'),
    path('tasks/done/<int:id>', views.donetask, name='donetask'),
    path('createproject/', views.createproject, name='create_project'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log, name='login'),
    path('logout/', views.signout, name='logout'),
    path('task/<int:id>', views.taskdetail, name='taskdetail')
    
]