import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("─────────────────────")
    activity = discord.Game(name="산에서 드리프트")
    await client.change_presence(status=discord.Status.online, activity=activity)

            
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("!글로벌밴"):
        embed = discord.Embed(title="💡 글로벌 밴 조치 방법",
        description="\n다운힐러즈는 FiveM 글로벌 밴에 대하여 논의 할 수 없습니다.\n FiveM 자체 내에서 지정한 추방이므로, FiveM 커뮤니티의 가이드라인 위반,\n이유 없음에 해당 됩니다. 만약 잘못된 조치라고 생각된다면,\n[https://forum.cfx.re/w/ban-report](https://forum.cfx.re/w/ban-report)\n으로 양식을 제출하시면 됩니다.",
        color=0x47ff5d)
        await message.channel.send(embed=embed)
    if "하위" in message.content:
        await message.channel.send("헤위~")
        return
    if "어이" in message.content:
        await message.channel.send("{0.author.name} 어서 오고".format(message))
        return
    if "ㅋㅋㅋㅋㅋㅋㅋㅋㅋ" in message.content:
        await message.channel.send("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
        return
    if "수듄" in message.content:
        await message.channel.send("수듄~")
        return
    response_1 = [
        "서버 열",
        "서버 언",
        "서버언",
        "열었"]
    for ask_1 in response_1:
        if ask_1 in message.content:
            server_status_channel = client.get_channel(615468836753375242)#서버 온/오프 채널
            await message.channel.send("안녕하세요 {0.author.mention}님 서버 오픈 관련은 {1.mention} 채널을 참고해주세요".format(message,server_status_channel))
            return

    

        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
