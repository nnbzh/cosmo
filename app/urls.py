from django.urls import path

from app import views

urlpatterns = [
    path('', views.all),
    path('<uuid:uuid>', views.get),
    path('new', views.post),

]
# path('todos/<int:todo_id>/tasks/completed', views.get_completed_tasks, name='completed_tasks'),
