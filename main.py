import random
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

joke_list = ['Говорят, если перевернуть табуретку, то на него можно будет посадить 4 коммуниста', 'Разница между коммунистом и маньяком заключается в том, что у маньяка есть цель']
random_joke = random.randint(0, len(joke_list) - 1)

# бот для команд, выданы все намерения
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
	print(f'{bot.user} запущен и готов к работе!\n')

@bot.event
async def on_message(message):
	# если сообщение от бота - игнорируем
	if message.author.bot:
		return
	# проверяем, является ли сообщение командой
	await bot.process_commands(message)


#парсер шутки 
def get_joke():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
    }

    url = f'{"https://randstuff.ru/joke/fav/"}'

    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text)
    joke_text = soup.find('td').text

    @bot.command(aliases=['joke', 'шутка'])
    async def joke_(ctx):
        await ctx.send((f'Шутка дня: {joke_text}'))
get_joke()


TOKEN = 'MTIwMzczNjc1MjI3MTkyMTI0Mg.Go3_Zu.sfpmBkQ6xaJZVCi2yIfIxC6NGsPL3ZFw_-u0AU' 
bot.run(TOKEN)
