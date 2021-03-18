import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!')
TOKEN = 'ODE5MTE1MDI2NDU0NTQ0NDE1.YEh6UA.rQJcY4WXa68VDbHMOyPz5G4drr4'

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('강의'))
    print('[알림][봇이 성공적으로 구동되었습니다.]')

@bot.event
async def on_message(msg):
    if msg.author.bot: return None
    await bot.process_commands(msg)

@bot.command()
async def 안녕(ctx):
    await ctx.channel.send('나도 안녕!')

bot.run(ODE5MTE1MDI2NDU0NTQ0NDE1.YEh6UA.rQJcY4WXa68VDbHMOyPz5G4drr4)