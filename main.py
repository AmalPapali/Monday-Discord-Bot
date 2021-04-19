import discord
import os
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
import random
import json
import time
import asyncio


client = discord.Client()
client = commands.Bot(command_prefix = 'm!')
client.remove_command('help')


@client.event

async def on_ready():
  print ('BOT HAS FINALLY BECOME ONLINE')
  await client.change_presence(status=discord.Status.online, activity = discord.Game("m!help for info/commands"))

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = '{:.2f} seconds still left on cooldown'.format(error.retry_after)
    await ctx.send(msg)


@client.command()
async def hello(ctx):
  await ctx.send('hello wassup')

@client.command()
@commands.has_permissions(kick_members=True)
async def clear(ctx, amount=10):
  await ctx.channel.purge(limit=amount)
  await ctx.send(f'Purged {amount} messages')
  time.sleep(1)
  await ctx.channel.purge(limit=1)

@client.command()
@commands.has_permissions(kick_members=True)
async def tempmute(ctx, member: discord.Member, mute_time : int):
  role = discord.utils.get(member.guild.roles, name='Hackerman Muted')
  await member.add_roles(role)
  await ctx.send(f'{member.mention} has been muted for {mute_time} seconds 😈')
  await asyncio.sleep(mute_time)
  await member.remove_roles(role)
  await ctx.send(f'{member.mention} has been unmuted')

@client.command()
async def invite(ctx):
  await ctx.send("Link to invite the bot to your different servers: ")
  await ctx.send("https://discord.com/api/oauth2/authorize?client_id=806197421528318003&permissions=8&scope=bot")

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
  "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
  "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
  "Yes.", "Yes – definitely.", "You may rely on it."]
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def add(ctx, a: int, b: int):
  embed = discord.Embed(title='Sum is', description=a+b, color=discord.Colour.orange())
  await ctx.send(embed=embed)

@client.command(aliases=['sub'])
async def subtract(ctx, a:int, b:int):
  embed = discord.Embed(title='Answer is', description=a-b, color=discord.Colour.orange())
  await ctx.send(embed=embed)

@client.command(aliases=['div'])
async def divide(ctx, a:int, b:int):
  await ctx.send("Answer is")
  await ctx.send(a/b)

@client.command(aliases=['mul'])
async def multiply(ctx, a:int, b:int):
  embed = discord.Embed(title='Product is', description=a*b, color=discord.Colour.orange())
  await ctx.send(embed=embed)

@client.command()
async def happy(ctx):
  await ctx.send('https://lh3.googleusercontent.com/-TDOZH1jyfrk/YHUKL5QbYRI/AAAAAAAAF5I/SGbTLDBvPy43laY2-wLDMZ8o1hvoztOPQCK8BGAsYHg/s0/2021-04-12.png?authuser=1')

@client.command()
async def greedy(ctx):
  await ctx.send('https://lh3.googleusercontent.com/-ZfLvnaSWp0s/YHUKXOgKuOI/AAAAAAAAAF0/jx7m5sFDNtQFE7YGEMjGPqbR5kZY4IdoQCK8BGAsYHg/s0/2021-04-12.png?authuser=0')

@client.command()
async def think(ctx):
  await ctx.send('https://lh3.googleusercontent.com/-RgUoJw3xe60/YHUJxmGaV9I/AAAAAAAAF5A/xk40NX3ux00Dmf2S-2uPqTQqAnUXhdg6ACK8BGAsYHg/s0/2021-04-12.png?authuser=1')

@client.command()
async def depressed(ctx):
  await ctx.send('https://lh3.googleusercontent.com/-8AGIUMTpdpg/YHnWNoVuWsI/AAAAAAAAF6E/Jl1Uyfwn7uw_TPm-_1DfYoyIzX2I5eCygCK8BGAsYHg/s0/2021-04-16.png?authuser=2')

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member, reason=None):
  role = discord.utils.get(member.guild.roles, name='Monday Muted')
  await member.add_roles(role)
  embed = discord.Embed(title=f"{member} has been muted", description=f'Reason: {reason}', color=discord.Colour.red())
  await ctx.send(embed=embed)

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member, reason=None):
  role = discord.utils.get(member.guild.roles, name='Monday Muted')
  await member.remove_roles(role)
  embed = discord.Embed(title=f"{member} has been unmuted", description=f"Reason: {reason}", color=discord.Colour.red())
  await ctx.send(embed=embed)





@client.group(pass_context=True, invoke_without_command=True, name='help')
async def help(ctx):
  embed=discord.Embed(title="Help", description="Use `m!help {category}` to get more info on each command.", color=discord.Colour.blue())
  embed.add_field(name="⚒️ Moderation", value="`m!help moderation`", inline=True) 
  embed.add_field(name="😎 Emotions", value="`m!help emotions`", inline=True)
  embed.add_field(name="🏫 School", value="`m!help school`", inline=True)
  embed.add_field(name="🔢 Math", value="`m!help math`", inline=True)
  embed.add_field(name="✨ Other", value="`m!help other`", inline=True)
  embed.set_thumbnail(url=str(client.get_user(806197421528318003).avatar_url))
  embed.set_footer(text="Bot created by mathkido, for any questions regarding bot please dm mathkido#8185")
  await ctx.send(embed=embed)


@help.command(name='moderation')
async def moderation(ctx):
  embed=discord.Embed(title="Moderation Help", description="Prefix is 'm!'. Must have the role 'Hackerman Muted' for the mute commands to work", color=discord.Colour.blue())
  embed.add_field(name="`m!kick`", value="Kicks a user from the server", inline=False) 
  embed.add_field(name="`m!ban`", value="Bans a user from the server", inline=False) 
  embed.add_field(name="`m!unban`", value="Unbans the user. Ex. m!unban Ajay the Awesome#1068 with the full username", inline=False)
  embed.add_field(name="`m!mute`", value="Mutes the user and they cannot talk until the admin unmutes them", inline=False) 
  embed.add_field(name="`m!unmute`", value="Unmutes the user, and they are able to talk", inline=False)  
  embed.add_field(name="`m!tempmute`", value="Mutes the user for a certain amount of time(measured in seconds) do m!tempmute {user} {time}", inline=False)  
  embed.add_field(name="`m!clear`", value="Clears the previous 10 messages from anyone", inline=False)
  embed.set_footer(text="Bot created by mathkido, for any questions regarding bot please dm mathkido#8185")
  embed.set_thumbnail(url=str(client.get_user(806197421528318003).avatar_url))
  await ctx.send(embed=embed)

@help.command(name='emotions')
async def emotion(ctx):
  embed=discord.Embed(title='Emotion Commands', description="Prefix is 'm!'. Emotion commands such as happy, and greedy will appear here", color=discord.Colour.blue())
  embed.add_field(name="`m!happy`", value="Sends a picture of someone happy", inline=True) 
  embed.add_field(name="`m!greedy`", value="Sends a picture of someone greedy", inline=False)
  embed.add_field(name="`m!think`", value="Sends a picture of someone thinking", inline=False)
  embed.add_field(name="`m!depressed`", value="Sends a picture of someone depressed", inline=False)
  embed.set_thumbnail(url=str(client.get_user(806197421528318003).avatar_url))
  embed.set_footer(text="Bot created by mathkido, for any questions regarding bot please dm mathkido#8185")  
  await ctx.send(embed=embed)

@help.command(name='school')
async def school(ctx):
  embed=discord.Embed(title='School Help', description="Prefix is 'm!'. School commands such as math help will appear here. For the core class help functions to work, you must have the roles 'Math Helper', 'Science Helper', 'Civics and History Helper', and 'ELA Helper'", color=discord.Colour.blue())
  embed.add_field(name="`m!mathelp`", value="Get math help from math helpers", inline=True) 
  embed.add_field(name="`m!sciencehelp`", value="Get science help from science helpers", inline=False) 
  embed.add_field(name="`m!elahelp`", value="Get ela help from ela helpers", inline=False) 
  embed.add_field(name="`m!historyhelp`", value="Get history help from history/civics helpers", inline=True) 
  embed.set_thumbnail(url=str(client.get_user(806197421528318003).avatar_url))
  embed.set_footer(text="Bot created by mathkido, for any questions regarding bot please dm mathkido#8185")
  await ctx.send(embed=embed)  

@help.command(name='math')
async def math(ctx):
  embed=discord.Embed(title='Math Commands', description="Prefix is 'm!'. Math commands such as add and multiply will appear here", color=discord.Colour.blue())
  embed.add_field(name="`m!add`", value="Adds two integers", inline=True) 
  embed.add_field(name="`m!subtract`", value="Subtracts two integers. Alternate command is 'sub'", inline=False)
  embed.add_field(name="`m!multiply`", value="Multiplies two integers. Alternate command is 'mul'", inline=False)
  embed.add_field(name="`m!divide`", value="Divides two integers. Alternate command is 'div'", inline=False)
  embed.set_thumbnail(url=str(client.get_user(806197421528318003).avatar_url))
  embed.set_footer(text="Bot created by mathkido, for any questions regarding bot please dm mathkido#8185")  
  await ctx.send(embed=embed)

@help.command(name='other')
async def other(ctx):
  embed=discord.Embed(title='Other Commands', description="Prefix is 'm!'. Other commands will appear here.", color=discord.Colour.blue())
  embed.add_field(name="`m!hello`", value="Returns with hello wassup", inline=False) 
  embed.add_field(name="`m!invite`", value="Brings up the link to invite this bot to your different servers", inline=False) 
  embed.add_field(name="`m!8ball`", value="Enter 'm!8ball {question} and get a random answer for it'", inline=False) 
  embed.set_footer(text="Bot created by mathkido, for any questions regarding bot please dm mathkido#8185")
  await ctx.send(embed=embed)







'''
@client.command(pass_context=True)
async def help(ctx):
  embed=discord.Embed(title="Help", description="Prefix is 'm!'. Find different commands and their descriptions. For the core class help functions to work, you must have the roles 'Math Helper', 'Science Helper', 'Civics and History Helper', and 'ELA Helper'", color=discord.Colour.blue())
  embed.add_field(name="hello", value="Returns with hello wassup", inline=False) 
  embed.add_field(name="mathelp", value="Get math help from math helpers", inline=True) 
  embed.add_field(name="sciencehelp", value="Get science help from science helpers", inline=False) 
  embed.add_field(name="elahelp", value="Get ela help from ela helpers", inline=False) 
  embed.add_field(name="historyhelp", value="Get history help from history/civics helpers", inline=True) 
  embed.add_field(name="invite", value="Brings up the link to invite this bot to your different servers", inline=False) 
  embed.add_field(name="8ball", value="Enter 'm!8ball {question} and get a random answer for it'", inline=False) 
  embed.add_field(name="help2", value="Brings up help command for moderation events and 2 column of commands", inline=False) 
  embed.add_field(name="help3", value="Brings up help command for emotion commands and 3rd column of commands", inline=False) 
  embed.add_field(name="help4", value="Brings up help command for math commands and 4th column of commands", inline=False) 
  embed.set_footer(text="Bot created by mathkido, for any questions regarding bot please dm mathkido#8185")
  await ctx.send(embed=embed)


@client.command(pass_context=True)
async def help2(ctx):
  embed=discord.Embed(title='Moderation Help', description="Prefix is 'm!'. Moderation events such as kick, ban will appear here", color=discord.Colour.blue())
  embed.add_field(name="kick", value="Kicks a user from the server", inline=False) 
  embed.add_field(name="ban", value="Bans a user from the server", inline=False) 
  embed.add_field(name="unban", value="Unbans the user. Ex. m!unban Ajay the Awesome#1068 with the full username", inline=False)
  embed.add_field(name="mute", value="Mutes the user and they cannot talk until the admin unmutes them", inline=False) 
  embed.add_field(name="unmute", value="Unmutes the user, and they are able to talk", inline=False)  
  embed.add_field(name="clear", value="Clears the previous 10 messages from anyone", inline=False)
  embed.set_footer(text="Bot created by mathkido, for any questions regarding bot please dm mathkido#8185")
  await ctx.send(embed=embed)

@client.command(pass_context=True)
async def help3(ctx):
  embed=discord.Embed(title='Emotion Commands', description="Prefix is 'm!'. Emotion commands such as happy, and greedy will appear here", color=discord.Colour.blue())
  embed.add_field(name="happy", value="Sends a picture of someone happy", inline=True) 
  embed.add_field(name="greedy", value="Sends a picture of someone greedy", inline=False)
  embed.add_field(name="think", value="Sends a picture of someone thinking", inline=False)
  embed.add_field(name="depressed", value="Sends a picture of someone depressed", inline=False)
  embed.set_footer(text="Bot created by mathkido, for any questions regarding bot please dm mathkido#8185")  
  await ctx.send(embed=embed)

@client.command(pass_context=True)
async def help4(ctx):
  embed=discord.Embed(title='Math Commands', description="Prefix is 'm!'. Math commands such as add and multiply will appear here", color=discord.Colour.blue())
  embed.add_field(name="add", value="Adds two integers", inline=True) 
  embed.add_field(name="subtract", value="Subtracts two integers", inline=False)
  embed.add_field(name="multiply", value="Multiplies two integers", inline=False)
  embed.add_field(name="divide", value="Divides two integers", inline=False)
  embed.set_footer(text="Bot created by mathkido, for any questions regarding bot please dm mathkido#8185")  
  await ctx.send(embed=embed)'''

@client.command()
@commands.cooldown(1,300,commands.BucketType.user)
async def mathelp(ctx):
  math = get(ctx.guild.roles, name='Math Helper')
  await ctx.send(f"{math.mention}, {ctx.message.author.mention} requires help, please don't spam this command ")

@client.command()
@commands.cooldown(1,300,commands.BucketType.user)
async def sciencehelp(ctx):
  science = get(ctx.guild.roles, name='Science Helper')
  await ctx.send(f"{science.mention}, {ctx.message.author.mention} requires help, please don't abuse command and spam it")

@client.command()
@commands.cooldown(1,300,commands.BucketType.user)
async def historyhelp(ctx):
  history = get(ctx.guild.roles, name='Civics and History Helper')
  await ctx.send(f"{history.mention}, {ctx.message.author.mention} requires help, don't abuse command")

@client.command()
@commands.cooldown(1,300,commands.BucketType.user)
async def elahelp(ctx):
  ela = get(ctx.guild.roles, name='ELA Helper')
  await ctx.send(f"{ela.mention}, {ctx.message.author.mention} requires help, don't abuse")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    embed=discord.Embed(title="Member kicked", description="Member has been kicked by an administrator for violating the rules", color=discord.Colour.green())
    await member.kick(reason=reason)
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
  embed=discord.Embed(title="Member banned", description="Member has been banned by an admin for violating the rules", color=discord.Colour.green())
  await member.ban(reason=reason)
  await ctx.send(embed=embed)
  await ctx.send(f'User {member.mention} has been banned')

@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f"Unbanned {user.mention}")
      return




client.run(os.getenv('TOKEN'))
