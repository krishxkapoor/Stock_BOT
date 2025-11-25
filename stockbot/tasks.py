from celery import shared_task
from .models import Alert
from .providers import get_latest_price
from django.contrib.auth.models import User
# from .tg_bot import send_telegram_message  # Implement later

@shared_task
def alert_checker():
    alerts = Alert.objects.filter(is_active=True)
    for alert in alerts:
        price = get_latest_price(alert.symbol)
        if price is None: continue
        if alert.alert_type == "price" and price >= alert.value:
            # send_telegram_message(alert.user.id, f"🚨 {alert.symbol} > {alert.value} (Current: {price})")
            alert.is_active = False
            alert.save()