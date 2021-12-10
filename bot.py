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
        
        elif command == "참새핀도르":
            try:
                fa = open("C:\\Users\\User\\Desktop\\봇\\참새핀도르.txt", 'a')
                

                data = "o\n"
                fa.write(data)

                if message.author.dm_channel:
                    await message.author.dm_channel.send("참새핀도르의 교실에 출석하셨습니다.\n오늘도 호구와트 독서실을 찾아주셔서 감사합니다.")
                elif message.author.dm_channel is None:
                    channel = await message.author.create_dm()
                    await channel.send("참새핀도르의 교실에 출석하셨습니다.\n오늘도 호구와트 독서실을 찾아주셔서 감사합니다.")

                await message.channel.send("출석체크 되었다.")
            except:
                print("error")

        elif command == "코풀푸프":
            try:
                fa = open("C:\\Users\\User\\Desktop\\봇\\코풀푸프.txt", 'a')
                

                data = "o\n"
                fa.write(data)

                if message.author.dm_channel:
                    await message.author.dm_channel.send("코풀푸프의 교실에 출석하셨습니다.\n오늘도 호구와트 독서실을 찾아주셔서 감사합니다.")
                elif message.author.dm_channel is None:
                    channel = await message.author.create_dm()
                    await channel.send("코풀푸프의 교실에 출석하셨습니다.\n오늘도 호구와트 독서실을 찾아주셔서 감사합니다.")

                await message.channel.send("출석체크 되었다.")
            except:
                print("error")
            
        elif command == "래번손톱":
            try:
                fa = open("C:\\Users\\User\\Desktop\\봇\\래번손톱.txt", 'a')
                

                data = "o\n"
                fa.write(data)

                if message.author.dm_channel:
                    await message.author.dm_channel.send("래번손톱의 교실에 출석하셨습니다.\n오늘도 호구와트 독서실을 찾아주셔서 감사합니다.")
                elif message.author.dm_channel is None:
                    channel = await message.author.create_dm()
                    await channel.send("래번손톱의 교실에 출석하셨습니다.\n오늘도 호구와트 독서실을 찾아주셔서 감사합니다.")
            except:
                print("error")

            await message.channel.send("출석체크 되었다.")

        elif command == "마른데린":
            try:
                fa = open("C:\\Users\\User\\Desktop\\봇\\마른데린.txt", 'a')
                

                data = "o\n"
                fa.write(data)

                if message.author.dm_channel:
                    await message.author.dm_channel.send("마른데린의 교실에 출석하셨습니다.\n오늘도 호구와트 독서실을 찾아주셔서 감사합니다.")
                elif message.author.dm_channel is None:
                    channel = await message.author.create_dm()
                    await channel.send("마른데린의 교실에 출석하셨습니다.\n오늘도 호구와트 독서실을 찾아주셔서 감사합니다.")
            except:
                print("error")
            await message.channel.send("출석체크 되었다.")

        elif command == "반대항결과":
            try:
                mr = open("C:\\Users\\User\Desktop\\봇\\마른데린.txt", 'r')
                lr = open("C:\\Users\\User\Desktop\\봇\래번손톱.txt", 'r')
                cr = open("C:\\Users\\User\\Desktop\\봇\\코풀푸프.txt", 'r')
                chr = open("C:\\Users\\User\\Desktop\\봇\\참새핀도르.txt", 'r')

                chamsaes = chr.readlines
                cofulfues = cr.readlines
                lebunclaws = lr.readlines
                maruns = mr.readlines

                await message.channel.send("마른데린: " + len(maruns))
                await message.channel.send("래번손톱: " + len(lebunclaws))
                await message.channel.send("코풀푸프: " + len(cofulfues))
                await message.channel.send("참새핀도르: " + len(chamsaes))
            except:
                print("error")
        
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
