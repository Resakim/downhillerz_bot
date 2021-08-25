import discord
import os

client = discord.Client()

@Client.event

async def on_ready():
    print("login")
    await client.change_presence(game=discord.Game(name='', type=1))
    



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
