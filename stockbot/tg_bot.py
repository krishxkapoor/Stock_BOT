from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from django.conf import settings
from .providers import fetch_ohlcv
from .signals import compute_indicators, score_signal
from .charting import plot_candlestick

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

async def send_telegram_message(user_id, text, image_b64=None):
    await bot.send_message(user_id, text)
    if image_b64:
        await bot.send_photo(user_id, photo=image_b64)

@dp.message_handler(commands=['start'])
async def start_cmd(message: Message):
    await message.reply("Welcome to Indian StockBot. Try /signal SYMBOL or /chart SYMBOL")

@dp.message_handler(commands=['signal'])
async def signal_cmd(message: Message):
    symbol = message.get_args().upper().split()[0]
    df = fetch_ohlcv(symbol)
    if df is None or df.empty:
        await message.reply(f"Couldn't fetch data for {symbol}. Is it an NSE ticker?")
        return
    df2 = compute_indicators(df)
    scores = score_signal(df2)
    await message.reply(
        f"{symbol} Signal:\nBuy: {scores['buy_prob']}%\nHold: {scores['hold_prob']}%\nSell: {scores['sell_prob']}%"
    )

@dp.message_handler(commands=['chart'])
async def chart_cmd(message: Message):
    symbol = message.get_args().upper().split()[0]
    df = fetch_ohlcv(symbol)
    if df is None or df.empty:
        await message.reply(f"Couldn't fetch data for {symbol}.")
        return
    df2 = compute_indicators(df)
    image_b64 = plot_candlestick(df2, symbol)
    await bot.send_photo(message.chat.id, photo=image_b64, caption=f"{symbol} Chart")
# Add /alert, /price, /watchlist logic as needed
