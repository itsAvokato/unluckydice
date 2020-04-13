import discord
from discord.ext import commands
from random import randint
import d20

BOT_PREFIX='!'
client=commands.Bot(command_prefix=BOT_PREFIX, help_command=None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("D&D 5e"))
    print('{0.user} - готов!'.format(client))
   
@client.command()
async def dnd(ctx, day, time, info):
    embed = discord.Embed(title="Dungeons & Dragons", colour=discord.Colour(0x80a146))
    embed.set_thumbnail(url="https://i.pinimg.com/originals/48/cb/53/48cb5349f515f6e59edc2a4de294f439.png")
    #embed.set_author(name="🐲", icon_url="https://i.pinimg.com/originals/48/cb/53/48cb5349f515f6e59edc2a4de294f439.png")
    embed.set_footer(text="Tabletop Simulator",
    icon_url="https://i.imgur.com/v7wPdWz.png")
    embed.add_field(name="Мастер:", value="<@!196262652153036800>", inline=False)
    embed.add_field(name="Дата:", value=day, inline=False)
    embed.add_field(name="Время:", value=time, inline=False)
    embed.add_field(name="Доп. инфо:", value=info, inline=False)
    embed.add_field(name="Игроки:", value="""
<@!287310543948218387>, <@!196263401209462784>, <@!371323670687383552>, 
<@!218046649954598913>, <@!371342008528273408>, <@!137269920202227713>""")

    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)

@client.command()
async def r(ctx, msg):
    result=d20.roll(msg)
    prnt=("{}\n🎲 {}".format(ctx.author.mention, result))
    await ctx.send(prnt)

@client.command()
async def gg(ctx):
    r1 = d20.roll("4d6kh3")
    r2 = d20.roll("4d6kh3")
    r3 = d20.roll("4d6kh3")
    r4 = d20.roll("4d6kh3")
    r5 = d20.roll("4d6kh3")
    r6 = d20.roll("4d6kh3")
    result=("{}\n**Генерирую...🎲** \n{}\n{}\n{}\n{}\n{}\n{}".format(ctx.author.mention, r1, r2, r3, r4, r5, r6))
    await ctx.send(result)
    
client.run('MTk3NjY0NjQwMDIzNTI3NDI1.Xkz5Ag.lW97Ez6g9IZheuYUXX1jSZLiIiA')
