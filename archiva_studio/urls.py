from django.urls import path
from stockbot.views import telegram_webhook

urlpatterns = [
    path('api/telegram/', telegram_webhook),
]