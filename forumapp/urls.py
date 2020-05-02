from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='user_login'),
    path('home/<str:name>', views.home, name='view_home'),
    path('register', views.register, name='user_register'),
    path('ask_questions/<str:name>/', views.askquestion, name='ask_questions'),
    path('view_answers/<int:id>/<str:name>', views.viewanswers, name='view_answers'),
    path('delete_question/<str:name>/<int:id>', views.deletequestion, name='delete_question'),
    path('edit_question/<str:name>/<str:action>/<int:id>', views.editquestion, name='edit_question'),
    path('comment/<int:id>/<str:name>/<int:qid>', views.comment, name='comment'),
    path('check/<str:name>/<str:action>/<int:id>', views.check, name='check'),
]
