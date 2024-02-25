

from django.urls import path

from .views import *

app_name = 'Message'
urlpatterns = [
    path('Chats/', TotalChatView.as_view(), name='Chats') ,
    path('chat2to2/<str:username>' , ChatBetweenView.as_view() , name='chat2to2') ,
]