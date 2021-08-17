from django.urls import path
from . import views
from .views import add_todo, signout, delete_todo, change_todo

urlpatterns = [
    path('home', views.index, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('add_todo', add_todo),
    path('delete-todo<int:id>', delete_todo),
    path('change-status<int:id>/<str:status>', change_todo),
    path('logout', signout),
]

