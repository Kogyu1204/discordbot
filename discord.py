import discord
improt os


client = discord.client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='프로그래밍', type=1))

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await client.send_message(message.channel, "안녕")


        acces_token = os.environ["BOT_TOKEN"]
        client.run(acces_token)
