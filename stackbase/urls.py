from django.urls import path
from . import views

app_name = 'stackbase'

urlpatterns = [
    path('', views.home, name="home"),

    #CRUD Methods
    path('questions/', views.QuestionListView.as_view(), name="questionList"),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name="questionDetail"),
    path('questions/<int:pk>/update/', views.QuestionUpdateView.as_view(), name="questionUpdate"),
    path('questions/<int:pk>/delete/', views.QuestionDeleteView.as_view(), name="questionDelete"),
    path('questions/<int:pk>/comment/', views.AddCommentView, name="addComment"),
    path('questions/ask/', views.QuestionCreateView.as_view(), name="questionAsk"),
]
