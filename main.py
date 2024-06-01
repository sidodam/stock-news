import asyncio
from finvizfinance.quote import finvizfinance
from aiogram import types, Dispatcher, Bot
from aiogram.filters import Command

from token_api import TOKEN

bot = Bot(token=TOKEN)
dispatcher = Dispatcher()

@dispatcher.message(Command('start'))
async def cmd_start(msg: types.Message) -> None:
    """Handle start command"""
    reply_text = f'Hello, {msg.from_user.first_name}! Send me a stock ticker to get the latest news.'

    await msg.reply(text=reply_text)

@dispatcher.message(~Command('news'))
async def cmd_news(msg: types.Message) -> None:
    """Handle stock ticker input"""
    ticker = msg.text.upper()
    try:
        stock = finvizfinance(ticker)
        news = stock.ticker_news()

        print(stock)
        reply_text = f"Latest news for {ticker}:\n\n{news}"
    except Exception as e:
        reply_text = f"{ticker} DOES NOT EXIST or an error occurred: {e}"


    await msg.reply(text=reply_text)

async def main() -> None:
    """Entry point"""
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())