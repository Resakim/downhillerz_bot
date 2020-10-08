import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("─────────────────────")
    activity = discord.Game(name="산에서 드리프트 중")
    await client.change_presence(status=discord.Status.online, activity=activity)

            
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    response_1 = [
        "서버 열",
        "서버 언",
        "서버언"]
    for ask_1 in response_1:
        if ask_1 in message.content:
            server_status_channel = client.get_channel(615468836753375242)#서버 온/오프 채널
            await message.channel.send("안녕하세요 {0.author.mention}님 서버 오픈 관련은 {1.mention} 채널을 참고해주세요".format(message,server_status_channel))

    

        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
