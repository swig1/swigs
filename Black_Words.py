import discord
from discord import *
import asyncio

INTENTS = Intents.all()
client = discord.Client(command_prefix = "",intents=INTENTS)
TOKEN = "토큰"

@client.event
async def on_ready(): 
    print("MADE BY SWIG")
    print(f"{client.user}")

@client.event
async def on_message(message):    
    if "시발" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "씨발" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)
    
    if "ㅗ" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)
    
    if "닥쳐" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)
    
    if "새끼" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)
    
    if "미친" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)
    
    if "애미" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)
    
    if "느금마" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)
    
    if "스발" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)
    
    if "tlqkf" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)
    
    if "^^발" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)
    
    if "후장" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "무친" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "싀발" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)
    
    if "또라이" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "ㅄ" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)
    
    if "ㅅㅂ" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "ㄷㅊ" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "ㅈㄹ" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "지랄" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "쓰레기" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "놈" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "고아" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "농아" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "이기야" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "게이" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "능지처참" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "노무현" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "운지" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "응디" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "ㅈ같은" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "보지" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "자지" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "색스" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "ㅅㅅ" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "고추" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "짬지" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

    if "찌찌" in message.content:
        await message.delete()
        금지어 = message.content[0:]
        embed = discord.Embed(title="🚫 SWIG 금지어 감지 시스템", description="> 채팅창에서 금지어가 감지되었습니다.\n> \n> 감지자 : {}\n> \n> 감지내용 : __{}__".format(message.author.mention, 금지어), color=0xFFFD05)
        await message.channel.send(embed=embed)

client.run(TOKEN)



