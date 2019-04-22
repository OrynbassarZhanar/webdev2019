from django.urls import path,re_path
from api import views

urlpatterns=[
    path('task_lists/', views.task_lists),
    path('task_lists/<int:pk>/tasks/<int:pk2>', views.task_lists_task),
    path('task_lists/<int:pk>/tasks/', views.task_lists_tasks),
    path('task_lists/<int:pk>', views.task_list)
]