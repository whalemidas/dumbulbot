import discord
import os
import random


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
        
    if command == "반배정":
            if message.author.get_roles is None:
                i = random.randrange(1,5)
                if i == 1:
                    role = discord.utils.get(msg.guild.roles, name="참새핀도르")
                    await message.author.add_roles(role)
                    await message.channel.send("흠...참새핀도르가 좋겠구나")
                if i == 2:
                    role = discord.utils.get(message.guild.roles, name = "마른데린")
                    await message.channel.send("어디보자.. 마른데린~")
                if i == 3:
                    role = discord.utils.get(message.guild.roles, name = "코풀푸프")
                    await message.channel.send("코풀푸프!")
                if i == 4:
                    role = discord.utils.get(message.guild.roles, name = "래번손톱")
                    await message.channel.send("래번손톱으로 배정되었다.")
            else:
                await message.channel.send("이미 반배정이 완료되었다.")

    

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
