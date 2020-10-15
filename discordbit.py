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
    if "하위" in message.content:
        await message.channel.send("헤위~")
    if "어이" in message.content:
        await message.channel.send("{0.author.name} 어서 오고".format(message))
    if "ㅋㅋㅋㅋㅋㅋ" in message.content:
        await message.channel.send("ㅋㅋㅋㅋㅋㅋㅋ")
    if "수듄" in message.content:
        await message.channel.send("수듄~")
    if "!글로벌밴" in message.content:
        await message.channel.send(":warning: 글로벌 밴 조치 방법
        다운힐러즈는 FiveM 글로벌 밴에 대하여 논의 할 수 없습니다.
        FiveM 자체 내에서 지정한 추방이므로, FiveM 커뮤니티의 가이드라인 미준수나
        이유 없음에 해당 됩니다. 만약 잘못된 조치라고 생각한다면,
        https://forum.cfx.re/w/ban-report 으로 양식을 제출하시면 됩니다.")
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
