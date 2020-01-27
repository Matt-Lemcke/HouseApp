from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDeleteView, TaskCompleteView
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('house/', views.house, name='house-settings'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:pk>/complete/',
         TaskCompleteView.as_view(), name='task-complete'),
    path('tasks/new/', TaskCreateView.as_view(), name='task-create'),
    path('calendar/', views.calendar, name='calendar'),
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name="task-delete"),
    path('house/create/', views.createhouse, name='house-create'),
    path('house/join/', views.joinhouse, name="house-join"),
    path('registration/createorjoin/', views.createorjoin, name="house-createorjoin"),
    path('splash/', views.splash, name="splash"),
    # path('addnote/', views.addnote, name="addnote"),
    # path('house/create/', CreateHouseView.as_view(), name='house-create'),
    # path('house/join/', JoinHouseView.as_view(), name='house-join'),
]
