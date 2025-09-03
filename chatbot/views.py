from django.shortcuts import render

# Create your views here.
import google.generativeai as genai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Configure Gemini
genai.configure(api_key=settings.GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message")
        response = chat.send_message(user_message)
        bot_reply = response.text
        return JsonResponse({"reply": bot_reply})
    return JsonResponse({"error": "Invalid request method"}, status=400)


def chat_page(request):
    return render(request, "chatbot/chat.html")