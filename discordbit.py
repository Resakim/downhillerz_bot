import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        print("login")
        print(self.user.name)
        print(self.user.id)
        print("─────────────────────")
        game = discord.Game("산에서 살어리랏다")
        await self.change_presence(status=discord.Status.online, activity=game)

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('안녕'):
            await message.channel.send('안녕하세요 {0.author.mention} 님'.format(message))

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
