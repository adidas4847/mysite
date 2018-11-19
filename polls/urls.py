from django.contrib import admin
from django.urls import path

from polls import views
from polls.views import index, detail, detail2, vote, save, edit

urlpatterns = [
    path('', index),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:num1>/<int:num2>', detail2),
    path('<int:question_id>/vote', vote),
    path('<int:question_id>/edit', edit),
    path('<int:question_id>/save', save),
]
