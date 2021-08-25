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
    if message.content.startswith("!help"):
        embed=discord.Embed(title=🚨 Report (신고) 가이드라인, description=작성 전 아래의 체크리스트를 참고, color=0xff2e2e)
        embed.set_thumbnail(url=https://cdn.discordapp.com/attachments/646497500299001876/879965785374740480/downhillerz_logo2.png)
        embed.add_field(name=1️⃣신고 대상자가 명확해야 합니다, value= 채팅, 인게임 닉네임은 관리자가 식별할 수 있어야 합니다., inline=True)
        embed.add_field(name=2️⃣신고 제보 작성요령, value=제보내용은 육하원칙에 따라 핵심을 쉽게 파악할 수 있도록 작성해야됩니다.\n 게임내 부정행위, 명예훼손등 왜 그런 일이 발생하게 되었는지\n 전 과정을 소상히 작성 부탁드립니다., inline=True)
        embed.add_field(name=3️⃣증거자료, value=이미지, 동영상, 링크 등으로 첨부합니다.\n 이는 필수적이며 미제출시 사실관계를 확인할 수 없습니다.\n (거짓진술 또는 본인에게 유리하게 편집, 왜곡하여 제출 시 신고자 처벌), inline=True)
        embed.add_field(name=❌아래에 해당하는 경우 신고가 처리되지 않습니다, value= , inline=True)
        embed.add_field(name=🔸사건 종료 이후 1시간 이상 경과된 사건, value= , inline=True)
        embed.add_field(name=🔸신고 대상자에게 거부의사를 명확히 알리지 않았을 경우, value= , inline=True)
        embed.add_field(name=🔸절차에 의하지 않고 자력으로 권리를 실현, 구제하는 경우, value=질서 위반행위에 대하여 처벌받을 수 있음, inline=True)
        embed.add_field(name=🔸신고 대상자가 사과를 했음에도 받아들여지지 않은 경우, value=사과의 진정성, 사건의 종결 상황에 따라 다를 수 있음, inline=True)
        embed.add_field(name=🔸패시브 모드(Passive)를 비활성화 한 차량충돌, value=주행로 외 주차된 차량을 고의로 파손한 행위는 제외, inline=True)
        embed.add_field(name=🔸관리자에게 불필요한 언행, 행동으로 분쟁 유발, value= , inline=True)
        embed.set_footer(text=⒞ Downhillerz)
        await message.channel.send(embed=embed)
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
