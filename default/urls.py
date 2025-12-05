from django.urls import path,include
from .views import poll_list, PollList, PollView,PollVote
urlpatterns=[
    path('',poll_list),
    path("list",PollList.as_view()),
    path("<int:pk>/",PollView.as_view(),name='poll_view'),
    path('<int:oid>/vote/',PollVote.as_view(),name='poll_vote'),
]