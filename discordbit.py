import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("─────────────────────")
    activity = discord.Game(name="산에서 살어리랏다")
    await client.change_presence(status=discord.Status.idle, activity=activity)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "하위" in message.content:
        await message.channel.send("안녕하세요")

    

        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
