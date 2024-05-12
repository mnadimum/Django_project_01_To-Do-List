from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLogInView, RegisterPage

from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views




urlpatterns = [
    #path('', views.tasklist, name='tasks'),
    path('login/', CustomLogInView.as_view(), name='login'),
    #path("accounts/login/", auth_views.LoginView.as_view(next_page = 'login')),
    #path('logout/', user_logout.views, name='logout'),
    #path('logout/', LogoutView.as_view(next_page = 'login/'), name='logout'),
    
    path('', TaskList.as_view(), name='tasks'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    
    

]
