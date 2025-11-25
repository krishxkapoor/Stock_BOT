import asyncio
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from aiogram import types
from .tg_bot import dp, bot

@csrf_exempt
@require_POST
def telegram_webhook(request):
    data = request.body.decode('utf-8')
    update = types.Update.de_json(data)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(dp.process_update(update))
    return JsonResponse({"ok": True})