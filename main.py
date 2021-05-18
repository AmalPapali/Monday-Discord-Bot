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
from datetime import date


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
    embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056")
    await ctx.send(embed=embed)

'''@client.event
async def on_message(message):
  if message.content == 'math link':
    await message.channel.send("https://scps.webex.com/meet/milanatz")
  if message.content == 'science link':
    await message.channel.send("https://scps.webex.com/meet/vannuybs")
  if message.content == 'marrero spanish link':
    await message.channel.send("https://scps.webex.com/webappng/sites/scps/meeting/download/ec398b13cb11c14d1de05c4c707ee2b0")
  if message.content == 'wtp link':
    await message.channel.send("Google Meet link: https://meet.google.com/umf-hjnc-fun\nZoom link: https://us02web.zoom.us/j/3393605376?pwd=d1IxQnBwVXlpTU1tOEYxSVlQenRiQT09")
  if message.content == 'testing schedule':
    await message.channel.send("https://lh3.googleusercontent.com/-f_E7PniU25w/YI87HuyDmvI/AAAAAAAAF-U/48p9JCtEgH4PEH-_6sMoUVL0d2FSHLkxgCK8BGAsYHg/s0/2021-05-02.png?authuser=4")'''


@client.command()
async def guess(ctx, number):
  number2guess = random.randint(0, 100)
  number = int(number)
  if number > number2guess:
    await ctx.send(f"{ctx.message.author} You were too high\nThe correct number was {number2guess}")
  elif number == number2guess:
    await ctx.send(f"{ctx.message.author} CORRECT. GREAT JOB\nThe number was indeed {number2guess}")

  elif number < number2guess:
    await ctx.send(f"{ctx.message.author} You were too low\nThe correct number was {number2guess}")
  else: 
    await ctx.send(f"{ctx.message.author} I didn't understand your response\nThe correct number was {number2guess}")

@client.command()
async def roll(ctx):
  number = random.randint(1, 6)
  await ctx.send(f"{number} was rolled")

@client.command()
async def flip(ctx):
  number = random.randint(1, 2)
  if number == 1:
    await ctx.send("Heads was flipped")
  if number == 2: 
    await ctx.send("Tails was flipped")

@client.command(aliases=["1min"])
async def mino(ctx):
  await ctx.send("The timer has started")
  await asyncio.sleep(60)
  await ctx.send("The timer is finished")

@client.command(aliases=["3min"])
async def mint(ctx):
  await ctx.send("The timer has started")
  await asyncio.sleep(180)
  await ctx.send("The timer is finished")

@client.command(aliases=["5min"])
async def minf(ctx):
  await ctx.send("The timer has started")
  await asyncio.sleep(300)
  await ctx.send("The timer is finished")

@client.command(aliases=["30min"])
async def minth(ctx):
  await ctx.send("The timer has started")
  await asyncio.sleep(1800)
  await ctx.send("The timer is finished")

@client.command(aliases=["1hr"])
async def minohr(ctx):
  await ctx.send("The timer has started")
  await asyncio.sleep(3600)
  await ctx.send("The timer is finished")

@client.command()
async def mins(ctx, amount):
  amount = amount*60
  await ctx.send("The timer has started")
  await asyncio.sleep(amount)
  await ctx.send("The timer is finished")

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
  sent = await channel.send(f"This suggestion was made by **{ctx.message.author}**\nSuggestion: **{suggestion}**")
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
async def bruhmoment(ctx):
  await ctx.send("https://lh3.googleusercontent.com/-GU4s-OE60I0/YJ1vBA1Xi2I/AAAAAAAAAGM/7vHK_j_3qfYXqmgIrycjnn016uRNYpAHQCK8BGAsYHg/s0/2021-05-13.png?authuser=0")

@client.command(aliases=['server', 'helpserver'])
async def help_server(ctx):
  await ctx.send("https://discord.gg/eM9SHEeW2f")

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
  await ctx.send('w')

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
async def join(ctx):
  channelid = client.get_channel(836327317994209320)
  channel = ctx.message.author.voice.channel
  await channel.connect()
  await channelid.send("I have joined the voice channel")

@client.command(pass_context=True)
async def leave(ctx):
  if (ctx.voice_client): # If the bot is in a voice channel 
    await ctx.guild.voice_client.disconnect()
    channelid = client.get_channel(836327317994209320)
    await channelid.send("I have left the voice channel")

@client.command()
async def youtube(ctx, *, search):
  standard = 'https://www.youtube.com/results?search_query='
  final = standard + search
  await ctx.send("This is what I have found:")
  await ctx.send(final)

@client.command()
async def imgur(ctx, *, search):
  standard = 'https://imgur.com/search?q='
  final = standard + search
  await ctx.send("This what I have found:")
  await ctx.send(final)

@client.command()
async def size(ctx):
  guild = ctx.guild
  await ctx.send(f"This server consists of: {ctx.guild.member_count} members") 

@client.command()
async def serverid(ctx):
  id = ctx.message.guild.id
  await ctx.send(f"Server ID: {id}")



@client.command()
async def serverinfo(ctx):
  id = ctx.message.guild.id
  guild = ctx.guild
  await ctx.send(f'Server Name: {guild.name}')
  await ctx.send(f"Server ID: {id}")
  await ctx.send(f"Server Member Count: {ctx.guild.member_count} members") 


#@client.command()
#async def spanish_marrero_link(ctx):
  
@client.command()
@commands.has_permissions(kick_members=True)
async def givept(ctx, member: discord.Member):
  channel = client.get_channel(840986859856855040)
  await channel.send(f"Congratulations on showing awesome behavior {member.mention}, {ctx.message.author} has recognized your awesome behavior")

@client.command()
async def report(ctx, member: discord.Member, *, reason):
  await ctx.channel.purge(limit=1)
  channel = client.get_channel(834469536052150352)
  await channel.send(f"Reporter: {ctx.message.author}\nReporting: {member}\nReason: {reason}")

@client.command()
@commands.has_permissions(kick_members=True)
async def staffreport(ctx, member: discord.Member, *, reason):
  await ctx.channel.purge(limit=1)
  channel = client.get_channel(835678385639915540)
  await channel.send(f"Reporter: {ctx.message.author}\nReporting: {member}\nReason: {reason}")


@client.command()
async def rps(ctx, move):
  possible_actions = ["rock", "paper", "scissors"]
  computer_action = random.choice(possible_actions)
  if move == computer_action:
    await ctx.send(f"Both players selected {move}. It's a tie!")
  elif move == "rock":
    if computer_action == "scissors":
        await ctx.send("Rock smashes scissors! You win!")
    else:
        await ctx.send("Paper covers rock! You lose.")
  elif move == "paper":
    if computer_action == "rock":
        await ctx.send("Paper covers rock! You win!")
    else:
        await ctx.send("Scissors cuts paper! You lose.")
  elif move == "scissors":
    if computer_action == "paper":
        await ctx.send("Scissors cuts paper! You win!")
    else:
        await ctx.send("Rock smashes scissors! You lose.")



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
  embed.add_field(name="🧮 Math Fun", value="`m!help mathfun`", inline=True)
  embed.add_field(name="🏀 Basketball", value="`m!help basketball`", inline=True)
  embed.add_field(name="⚡️ Server Related", value="`m!help related`", inline=True)
  embed.add_field(name="🎶 Music", value="`m!help music`", inline=True)
  embed.add_field(name="🔎 Search", value="`m!help search`", inline=True)
  embed.add_field(name="🎮 Games", value="`m!help games`", inline=True)
  embed.add_field(name="⏰ Timers", value="`m!help timers`", inline=True)
  embed.add_field(name="🎉 Birthdays", value="`m!help birthdays`", inline=True)
  embed.add_field(name="🪜 Levels", value="`m!help levels`", inline=True)
  embed.add_field(name="📝 Reports", value="`m!help reports`", inline=True)
  embed.add_field(name="⌨️ Links", value="`m!help links`", inline=True)
  embed.add_field(name="✨ Other", value="`m!help other`", inline=True)
  embed.set_thumbnail(url=str(client.get_user(806197421528318003).avatar_url))
  embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056")
  await ctx.send(embed=embed)

@help.command(name='birthdays')
async def birthdays(ctx):
  embed=discord.Embed(title='Birthday Commands', description="Prefix is `m!`. Birthday commands will appear here", color=discord.Colour.blue())
  embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056")  
  await ctx.send(embed=embed)

@help.command(name='links')
async def links(ctx):
  embed=discord.Embed(title='Class Link Commands', description="Prefix is `m!`. Class link commands will appear here", color=discord.Colour.blue())
  embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056")  
  await ctx.send(embed=embed)

@help.command(name='levels')
async def levels(ctx):
  embed=discord.Embed(title='Level Commands', description="Prefix is `m!`. Level commands will appear here", color=discord.Colour.blue())
  embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056")  
  await ctx.send(embed=embed)

@help.command(name='moderation')
async def moderation(ctx):
  embed=discord.Embed(title="Moderation Help", description="Prefix is `m!`. Must have the role 'Hackerman Muted' for the mute commands to work", color=discord.Colour.blue())
  embed.add_field(name="`m!kick`", value="Kicks a user from the server", inline=False) 
  embed.add_field(name="`m!ban`", value="Bans a user from the server", inline=False) 
  embed.add_field(name="`m!unban`", value="Unbans the user. Ex. m!unban Ajay the Awesome#1068 with the full username", inline=False)
  embed.add_field(name="`m!tempban`", value="Bans a user from the server for a certain amount of seconds", inline=False) 
  embed.add_field(name="`m!banish`", value="Banishes a user from the server and sends them to the ban redemption channel", inline=False) 
  embed.add_field(name="`m!unbanish`", value="Unbanishes a user from the server and allows them to access the rest of the server", inline=False) 
  embed.add_field(name="`m!mute`", value="Mutes the user and they cannot talk until the admin unmutes them", inline=False) 
  embed.add_field(name="`m!unmute`", value="Unmutes the user, and they are able to talk", inline=False)  
  embed.add_field(name="`m!tempmute`", value="Mutes the user for a certain amount of time(measured in seconds) do m!tempmute {user} {time}", inline=False)  
  embed.add_field(name="`m!clear`", value="Clears the previous 10 messages from anyone", inline=False)
  embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056")
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
  embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056")  
  await ctx.send(embed=embed)

@help.command(name='school')
async def school(ctx):
  embed=discord.Embed(title='School Help', description="Prefix is `m!`. School commands such as math help will appear here. For the core class help functions to work, you must have the roles 'Math Helper', 'Science Helper', 'Civics and History Helper', and 'ELA Helper'", color=discord.Colour.blue())
  embed.add_field(name="`m!mathelp`", value="Get math help from math helpers", inline=True) 
  embed.add_field(name="`m!sciencehelp`", value="Get science help from science helpers", inline=False) 
  embed.add_field(name="`m!elahelp`", value="Get ela help from ela helpers", inline=False) 
  embed.add_field(name="`m!historyhelp`", value="Get history help from history/civics helpers", inline=True) 
  embed.set_thumbnail(url=str(client.get_user(806197421528318003).avatar_url))
  embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056")
  await ctx.send(embed=embed)  

@help.command(name='math')
async def math(ctx):
  embed=discord.Embed(title='Math Commands', description="Prefix is `m!`. Math commands such as add and multiply will appear here", color=discord.Colour.blue())
  embed.add_field(name="`m!add`", value="Adds two integers", inline=True) 
  embed.add_field(name="`m!subtract`", value="Subtracts two integers. Alternate command is 'sub'", inline=False)
  embed.add_field(name="`m!multiply`", value="Multiplies two integers. Alternate command is 'mul'", inline=False)
  embed.add_field(name="`m!divide`", value="Divides two integers. Alternate command is 'div'", inline=False)
  embed.set_thumbnail(url=str(client.get_user(806197421528318003).avatar_url))
  embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056")  
  await ctx.send(embed=embed)

@help.command(name="related")
async def related(ctx):
  embed=discord.Embed(title='Server Related Helpful Commands', description="Prefix is `m!`. Server commands such as suggestion features will appear here.", color=discord.Colour.blue())
  embed.add_field(name="`m!suggest {suggestion}`", value="Posts your suggestion in the suggestion channel for others to vote on", inline=False) 
  embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056") 
  await ctx.send(embed=embed)

@help.command(name='music')
async def music(ctx):
  embed=discord.Embed(title='Music Commands', description="Prefix is `m!`. Music commands such as joining vc's will appear here.", color=discord.Colour.blue())
  embed.add_field(name="`m!join`", value="Joins the vc that the author is in", inline=False)
  embed.add_field(name="`m!leave`", value="Leaves the vc", inline=False) 
  embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056") 
  await ctx.send(embed=embed)

@help.command(name='timers')
async def timers(ctx):
  embed=discord.Embed(title='Music Commands', description="Prefix is `m!`. Timer commands such as 1 min timer will appear here.", color=discord.Colour.blue())
  embed.add_field(name="`m!1min`", value="1 minute timer", inline=False)
  embed.add_field(name="`m!3min`", value="3 minute timer", inline=False)
  embed.add_field(name="`m!5min`", value="5 minute timer", inline=False)
  embed.add_field(name="`m!30min`", value="30 minute timer", inline=False)
  embed.add_field(name="`m!1hr`", value="1 hour timer", inline=False)
  embed.add_field(name="`m!mins {time}`", value="A timer for {time} minutes", inline=False)
  embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056") 
  await ctx.send(embed=embed)

@help.command(name='search')
async def search(ctx):
  embed=discord.Embed(title='Search Commands', description="Prefix is `m!`. Music commands such as searching youtube will appear here.", color=discord.Colour.blue())
  embed.add_field(name="`m!youtube`", value="Searches youtube", inline=False)
  embed.add_field(name="`m!imgur`", value="Searches imgur", inline=False) 
  embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056") 
  await ctx.send(embed=embed)

@help.command(name='games')
async def games(ctx):
  embed=discord.Embed(title='Game Commands', description="Prefix is `m!`. Game commands will appear here.", color=discord.Colour.blue())
  embed.add_field(name="`m!givept`", value="Gives the user a rep point for displaying outstanding behavior", inline=False)
  embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056") 
  await ctx.send(embed=embed)

@help.command(name='reports')
async def reports(ctx):
  embed=discord.Embed(title='Report Commands', description="Prefix is `m!`. Report commands will appear here.", color=discord.Colour.blue())
  embed.add_field(name="`m!report`", value="Reports a user and allows others to vote if it is justified and the punishment", inline=False)
  embed.add_field(name="`m!staffreport`", value="Reports a user and allows others to vote if it is justified and the punishment", inline=False)
  embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056") 
  await ctx.send(embed=embed)

@help.command(name='other')
async def other(ctx):
  embed=discord.Embed(title='Other Commands', description="Prefix is `m!`. Other commands will appear here.", color=discord.Colour.blue())
  embed.add_field(name="`m!hello`", value="Returns with hello wassup", inline=False) 
  embed.add_field(name="`m!invite`", value="Brings up the link to invite this bot to your different servers", inline=False) 
  embed.add_field(name="`m!8ball`", value="Enter 'm!8ball {question} and get a random answer for it'", inline=False) 
  embed.add_field(name="`m!help_server`", value="Invite to the Monday Help Server. Alternate command for the same result is `m!server`", inline=False) 
  embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056")
  await ctx.send(embed=embed)

@help.command(name='mathfun')
async def mathfun(ctx):
  embed=discord.Embed(title='Math Game Commands', description="Prefix is `m!`. Fun math commands will appear here.", color=discord.Colour.blue())
  embed.add_field(name="`m!guess`", value="Guess a random number between 1 and 100", inline=False) 
  embed.add_field(name="`m!roll`", value="Rolls a 6 sided die", inline=False)
  embed.add_field(name="`m!flip`", value="Flips a coin", inline=False)
  embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056")
  await ctx.send(embed=embed)

@help.command(name='basketball')
async def basketball(ctx):
  embed=discord.Embed(title='Basketball Commands', description="Prefix is `m!`. Basketball commands will appear here.", color=discord.Colour.blue())
  embed.add_field(name="`m!curry`", value="Returns with Stephen Curry's picture", inline=False)
  embed.add_field(name="`m!lebron`", value="Returns with Lebron's picture", inline=False)
  embed.add_field(name="`m!irving`", value="Returns with Kyrie Irving's picture", inline=False)
  embed.add_field(name="`m!mj`", value="Returns with Michael Jordan's picture", inline=False)
  embed.add_field(name="`m!durant`", value="Returns with Kevin Durant's picture", inline=False)
  embed.set_footer(text="Bot created by DaBoss, for any questions regarding bot please dm DaBoss#9056")
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
