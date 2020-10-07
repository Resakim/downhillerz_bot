import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("─────────────────────")
    game = discord.Game("산에서 살어리랏다")
    await client.change_presence(status=discord.Status.online, activity=game)
    #await client.change_presence(activity=discord.Game(name="산에서 살어리랏다"))
    #await client.change_presence(game=discord.Game(name='산에서 살어리랏다', type=1))
    
@client.event
async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('안녕'):
            await message.channel.send('안녕하세요 {0.author.mention}님'.format(message))
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
