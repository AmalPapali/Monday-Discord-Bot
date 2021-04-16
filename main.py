import discord
import os
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import Cog

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
async def happy(ctx):
  await ctx.send('https://lh3.googleusercontent.com/-TDOZH1jyfrk/YHUKL5QbYRI/AAAAAAAAF5I/SGbTLDBvPy43laY2-wLDMZ8o1hvoztOPQCK8BGAsYHg/s0/2021-04-12.png?authuser=1')

@client.command()
async def greedy(ctx):
  await ctx.send('https://lh3.googleusercontent.com/-ZfLvnaSWp0s/YHUKXOgKuOI/AAAAAAAAAF0/jx7m5sFDNtQFE7YGEMjGPqbR5kZY4IdoQCK8BGAsYHg/s0/2021-04-12.png?authuser=0')

@client.command()
async def think(ctx):
  await ctx.send('https://lh3.googleusercontent.com/-RgUoJw3xe60/YHUJxmGaV9I/AAAAAAAAF5A/xk40NX3ux00Dmf2S-2uPqTQqAnUXhdg6ACK8BGAsYHg/s0/2021-04-12.png?authuser=1')

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
  role = discord.utils.get(member.guild.roles, name='Hackerman Muted')
  await member.add_roles(role)
  await ctx.send("Member Muted")

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
  role = discord.utils.get(member.guild.roles, name='Hackerman Muted')
  await member.remove_roles(role)
  await ctx.send('Member has been unmuted')

@client.command(pass_context=True)
async def help(ctx):
  embed=discord.Embed(title="Help", description="Prefix is 'm!'. Find different commands and their descriptions. For the core class help functions to work, you must have the roles 'Math Helper', 'Science Helper', 'Civics and History Helper', and 'ELA Helper'", color=discord.Colour.blue())
  embed.add_field(name="hello", value="Returns with hello wassup", inline=False) 
  embed.add_field(name="mathelp", value="Get math help from math helpers", inline=True) 
  embed.add_field(name="sciencehelp", value="Get science help from science helpers", inline=False) 
  embed.add_field(name="elahelp", value="Get ela help from ela helpers", inline=False) 
  embed.add_field(name="historyhelp", value="Get history help from history/civics helpers", inline=True) 
  embed.add_field(name="help2", value="Brings up help command for moderation events and 2 column of commands", inline=False) 
  embed.add_field(name="help3", value="Brings up help command for emotion commands and 3rd column of commands", inline=False) 
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
  embed.set_footer(text="Bot created by mathkido, for any questions regarding bot please dm mathkido#8185")
  await ctx.send(embed=embed)

@client.command(pass_context=True)
async def help3(ctx):
  embed=discord.Embed(title='Emotion Commands', description="Prefix is 'm!'. Emotion commands such as happy, and greedy will appear here", color=discord.Colour.blue())
  embed.add_field(name="happy", value="Sends a picture of someone happy", inline=True) 
  embed.add_field(name="greedy", value="Sends a picture of someone greedy", inline=False)
  embed.add_field(name="think", value="Sends a picture of someone thinking", inline=False)
  embed.set_footer(text="Bot created by mathkido, for any questions regarding bot please dm mathkido#8185")  
  await ctx.send(embed=embed)

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
    await member.kick(reason=reason)
    await ctx.send(f'User {member.mention} has been kicked')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
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
