# -- coding: utf-8 --

import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("─────────────────────")
    activity = discord.Game(name="집에서 교육")
    await client.change_presence(status=discord.Status.online, activity=activity)
    



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
