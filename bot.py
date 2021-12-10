import discord
import os



client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("호구와트 독서실 관리")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("안녕하세요"):
        await message.channel.send("그래")

    if message.content.startswith("덤불도어"):
        text = message.content.split
        command = message.content.split(" ")[1]

        if command == "인사":
            await message.channel.send("그래")
        
        
        
    if message.content.startswith("루모스"):
        await message.channel.send("빛이 당신의 어두운 미래를 밝게 비추었습니다.")
    
    if message.content.startswith("아바다케다브라"):
        await message.channel.send("당신의 공부를 방해하는 유혹에게 저주를 걸었습니다.")
    
    if message.content.startswith("아씨오"):
        await message.channel.send("뿌슝빠숑 휘유유우우웅(대충 뭔가 날아오는 소리)")
        
    if message.content.startswith("!고소"):
        attacker = message.content.split(" ")[1]
        victim = message.content.split(" ")[2]

        fa = open("C:\\Users\\User\\Desktop\\봇\\고소목록.txt", 'a')
        fa.write(victim + "님이 " + attacker + "님을 고소하셨습니다.\n")

        await message.channel.send("고소가 성공적으로 되었습니다.")

    

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
