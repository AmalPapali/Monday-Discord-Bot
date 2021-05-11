import discord
import os
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
import random
import json
import time
import asyncio
from discord import Permissions
from discord import DMChannel
from discord.ext import tasks

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
  if isinstance(error, commands.CommandNotFound):
    embed=discord.Embed(title="Command not found", description=f"{ctx.author.mention} That is not a valid command. Do `m!help` for help", colour=discord.Colour.purple())
    await ctx.send(embed=embed)


@client.command()
async def hello(ctx):
  await ctx.send('hello wassup')

@client.command()
async def warn(ctx):
  await ctx.send("You've been warned lol")

@client.command(aliases=["ms"])
async def ping(ctx): 
    await ctx.send(f"My ping is: {round(client.latency * 1000)} ms.")

@client.command()
async def qotd(ctx):
  await ctx.author.send("QOTD for today:")
  await ctx.author.send("||If you have only one match and you walked into a room where there was an oil burner, a kerosene lamp, and a wood burning stove, which one would you light first? - This is another easy common sense question, will move on from Monday||")

@client.command()
async def suggest(ctx, *, suggestion):
  await ctx.channel.purge(limit=1)
  guild_name = ctx.guild
  channel = client.get_channel(825117309941186560)
  #description = f"{ctx.message.author.mention} has suggested this suggestion."
  #value = f"{suggestion}"
  #author = ctx.message.author
  #embed=discord.Embed(title="Suggestion", description=f"Suggestion from {author}", color=discord.Colour.blue())
  #embed.add_field(name= "", value = "value", inline=True)
  #await channel.send(embed=embed)
  #sent = ""
  sent = await channel.send(f"This suggestion was made by {ctx.message.author}\nSuggestion: {suggestion}")
  emoji = '\N{THUMBS UP SIGN}'
  await sent.add_reaction(emoji)
  await sent.add_reaction('👎')
  #await sent.add_reaction("⬆️")
  #await sent.add_reaction("⬇️")



'''@client.command()
async def warnban(ctx, member: discord.Member, *, reason):
  mutedRole = await ctx.guild.create_role(name="Muted")
  for channel in ctx.guild.channels:
    await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_messages=False)
  await member.add_roles(mutedRole, reason=reason)'''

@client.command()
async def approve(ctx, member: discord.Member, *, suggestion):
  await ctx.channel.purge(limit=1)
  channel = client.get_channel(825117309941186560)
  await channel.send(f"{member.mention} your suggestion: {suggestion} has been approved.\nPlease wait for it to be implemented")

@client.command()
async def implemented(ctx, member: discord.Member, *, suggestion):
  await ctx.channel.purge(limit=1)
  channel = client.get_channel(825117309941186560)
  await channel.send(f"{member.mention} your suggestion: {suggestion} has been implemented.")


@client.command()
@commands.has_permissions(ban_members=True)
async def potdannounce(ctx, member: discord.Member, *, points):
  await ctx.channel.purge(limit=1)
  channel = client.get_channel(837700765203038269)
  message = (f'{member.mention} has solved the POTD and has earned {points} points')
  await channel.send(message)

@client.command()
@commands.has_permissions(ban_members=True)
async def qotdannounce(ctx, member: discord.Member, *, points):
  await ctx.channel.purge(limit=1)
  channel = client.get_channel(837700765203038269)
  message = (f'{member.mention} has solved the QOTD and has earned {points} points')
  await channel.send(message)

@client.command()
async def potd(ctx):
  await ctx.author.send("POTD for today")
  await ctx.author.send("https://cdn.discordapp.com/attachments/836410256992501780/837696991596249148/unknown.png")

@client.command()
async def curry(ctx):
  await ctx.send('https://lh3.googleusercontent.com/-xroNHJ_IHc4/YH-dDhDKSJI/AAAAAAAAF7E/MCTUvF8gHScHrn2OwNU71y05pkN0otT2gCK8BGAsYHg/s0/2021-04-20.png?authuser=2')

@client.command()
async def lebron(ctx):
  await ctx.send('https://lh3.googleusercontent.com/-XDPGHL5O9UY/YH-dSOyxLAI/AAAAAAAAF7I/3DCmKU1EbEM-ubmESkgErHJ2sfi96CUEQCK8BGAsYHg/s0/2021-04-20.png?authuser=2')

@client.command()
async def durant(ctx):
  await ctx.send('https://lh3.googleusercontent.com/-HraLvD49UbM/YH-ddkVMi0I/AAAAAAAAF7M/9f7lmy1Ttl8x-G2EoC7nYaUTNPdU_PIUwCK8BGAsYHg/s0/2021-04-20.png?authuser=2')

@client.command()
async def irving(ctx):
  await ctx.send('https://lh3.googleusercontent.com/-XvpMGUo4P9w/YH-dx0BgLjI/AAAAAAAAF7U/De4jRAAtQUs56YSrE1lnOPlZw5iI4vCSACK8BGAsYHg/s0/2021-04-20.png?authuser=2')

@client.command()
async def mj(ctx):
  await ctx.send('https://lh3.googleusercontent.com/-4ixrJGL1l6M/YH-d-io4OnI/AAAAAAAAF7Y/Fb55Cj1-BzUvw4E0T4uSuZRBZBdN_ZJSgCK8BGAsYHg/s0/2021-04-20.png?authuser=2')

@client.command()
@commands.has_permissions(kick_members=True)
async def clear(ctx, amount=10):
  await ctx.channel.purge(limit=amount)
  await ctx.send(f'Purged {amount} messages')
  time.sleep(1)
  await ctx.channel.purge(limit=1)

@client.command()
@commands.has_permissions(kick_members=True)
async def tempmute(ctx, member: discord.Member, mute_time : int, *, reason=None):
  role = discord.utils.get(member.guild.roles, name='Hackerman Muted')
  await member.add_roles(role)
  await ctx.send(f'{member.mention} has been muted for {mute_time} seconds 😈 Reason: {reason}')
  await asyncio.sleep(mute_time)
  await member.remove_roles(role)
  await ctx.send(f'{member.mention} has been unmuted')

@client.command()
@commands.has_permissions(ban_members=True)
async def banish(ctx, member: discord.Member, *, reason=None):
  role = discord.utils.get(member.guild.roles, name='BANISHED')
  await member.add_roles(role)
  channel = client.get_channel(841004263693746247)
  await channel.send(f"{member.mention} WELCOME TO THE BANISHED CLUB. All idiots such as you will end up here\nThe reason for this was: {reason}")


@client.command()
@commands.has_permissions(ban_members=True)
async def unbanish(ctx, member: discord.Member, *, reason=None):
  role = discord.utils.get(member.guild.roles, name='BANISHED')
  channel = client.get_channel(841004263693746247)
  await channel.send(f"{member.mention} Good Job, you have been unbanished")
  time.sleep(5)
  await member.remove_roles(role)

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

'''@client.command()
async def roast(ctx, member : discord.Member):
  roasts = []
  await ctx.send(f'')'''

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
async def mute(ctx, member: discord.Member, *, reason=None):
  role = discord.utils.get(member.guild.roles, name='Hackerman Muted')
  await member.add_roles(role)
  embed = discord.Embed(title=f"{member} has been muted", description=f'Reason: {reason}', color=discord.Colour.red())
  await ctx.send(embed=embed)

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member, *,reason=None):
  role = discord.utils.get(member.guild.roles, name='Hackerman Muted')
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
  embed.add_field(name="🏀 Basketball", value="`m!help basketball`", inline=True)
  embed.add_field(name="✨ Other", value="`m!help other`", inline=True)
  embed.set_thumbnail(url=str(client.get_user(806197421528318003).avatar_url))
  embed.set_footer(text="Bot created by mathkido, for any questions regarding bot please dm mathkido#8185")
  await ctx.send(embed=embed)


@help.command(name='moderation')
async def moderation(ctx):
  embed=discord.Embed(title="Moderation Help", description="Prefix is `m!`. Must have the role 'Hackerman Muted' for the mute commands to work", color=discord.Colour.blue())
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
  embed=discord.Embed(title='Emotion Commands', description="Prefix is `m!`. Emotion commands such as happy, and greedy will appear here", color=discord.Colour.blue())
  embed.add_field(name="`m!happy`", value="Sends a picture of someone happy", inline=True) 
  embed.add_field(name="`m!greedy`", value="Sends a picture of someone greedy", inline=False)
  embed.add_field(name="`m!think`", value="Sends a picture of someone thinking", inline=False)
  embed.add_field(name="`m!depressed`", value="Sends a picture of someone depressed", inline=False)
  embed.set_thumbnail(url=str(client.get_user(806197421528318003).avatar_url))
  embed.set_footer(text="Bot created by mathkido, for any questions regarding bot please dm mathkido#8185")  
  await ctx.send(embed=embed)

@help.command(name='school')
async def school(ctx):
  embed=discord.Embed(title='School Help', description="Prefix is `m!`. School commands such as math help will appear here. For the core class help functions to work, you must have the roles 'Math Helper', 'Science Helper', 'Civics and History Helper', and 'ELA Helper'", color=discord.Colour.blue())
  embed.add_field(name="`m!mathelp`", value="Get math help from math helpers", inline=True) 
  embed.add_field(name="`m!sciencehelp`", value="Get science help from science helpers", inline=False) 
  embed.add_field(name="`m!elahelp`", value="Get ela help from ela helpers", inline=False) 
  embed.add_field(name="`m!historyhelp`", value="Get history help from history/civics helpers", inline=True) 
  embed.set_thumbnail(url=str(client.get_user(806197421528318003).avatar_url))
  embed.set_footer(text="Bot created by mathkido, for any questions regarding bot please dm mathkido#8185")
  await ctx.send(embed=embed)  

@help.command(name='math')
async def math(ctx):
  embed=discord.Embed(title='Math Commands', description="Prefix is `m!`. Math commands such as add and multiply will appear here", color=discord.Colour.blue())
  embed.add_field(name="`m!add`", value="Adds two integers", inline=True) 
  embed.add_field(name="`m!subtract`", value="Subtracts two integers. Alternate command is 'sub'", inline=False)
  embed.add_field(name="`m!multiply`", value="Multiplies two integers. Alternate command is 'mul'", inline=False)
  embed.add_field(name="`m!divide`", value="Divides two integers. Alternate command is 'div'", inline=False)
  embed.set_thumbnail(url=str(client.get_user(806197421528318003).avatar_url))
  embed.set_footer(text="Bot created by mathkido, for any questions regarding bot please dm mathkido#8185")  
  await ctx.send(embed=embed)

@help.command(name='other')
async def other(ctx):
  embed=discord.Embed(title='Other Commands', description="Prefix is `m!`. Other commands will appear here.", color=discord.Colour.blue())
  embed.add_field(name="`m!hello`", value="Returns with hello wassup", inline=False) 
  embed.add_field(name="`m!invite`", value="Brings up the link to invite this bot to your different servers", inline=False) 
  embed.add_field(name="`m!8ball`", value="Enter 'm!8ball {question} and get a random answer for it'", inline=False) 
  embed.set_footer(text="Bot created by mathkido, for any questions regarding bot please dm mathkido#8185")
  await ctx.send(embed=embed)


@help.command(name='basketball')
async def basketball(ctx):
  embed=discord.Embed(title='Basketball Commands', description="Prefix is `m!`. Basketball commands will appear here.", color=discord.Colour.blue())
  embed.add_field(name="`m!curry`", value="Returns with Stephen Curry's picture", inline=False)
  embed.add_field(name="`m!lebron`", value="Returns with Lebron's picture", inline=False)
  embed.add_field(name="`m!irving`", value="Returns with Kyrie Irving's picture", inline=False)
  embed.add_field(name="`m!mj`", value="Returns with Michael Jordan's picture", inline=False)
  embed.add_field(name="`m!durant`", value="Returns with Kevin Durant's picture", inline=False)
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
async def tempban(ctx, member: discord.Member, time:int, *, reason=None):
  username = client.get_user(member)
  user = await client.fetch_user(username)
  await DMChannel.send(username, f"You will be unbanned in {time} seconds")
  await DMChannel.send(username, "https://discord.gg/u7ZbF3qaQX")
  await member.ban(reason=reason)
  await ctx.send(f'User {member.mention} has been banned')
  await asyncio.sleep(time)
  banned_users = await ctx.guild.bans()
  for ban_entry in banned_users:
    user = ban_entry.user
  await ctx.guild.unban(user)
  await ctx.send(f"Unbanned {user.mention}")
  return

  
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
  await ctx.send(f"Unbanned {user.mention}")
  



client.run(os.getenv('TOKEN'))
