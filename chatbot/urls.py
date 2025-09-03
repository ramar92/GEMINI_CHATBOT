# chatbot/urls.py
from django.urls import path
from .views import chatbot_view, chat_page

urlpatterns = [
    path("chat/", chat_page, name="chat_page"),   # Renders the page
    path("api/", chatbot_view, name="chatbot_api")  # Handles POST messages
]
