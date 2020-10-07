import discord


client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("─────────────────────")
    activity = discord.Game(name="Downhillerz")
    await client.change_presence(status=discord.Status.online, activity=activity)




access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
