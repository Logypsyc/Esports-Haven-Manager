import discord
import os
import random
from keep_alive import keep_alive
from discord.ext import commands
from dotenv import load_dotenv
import music
cogs = [music]

keep_alive()
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='$', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(bot)

@bot.command()
async def verify(ctx, *args):
  info = []
  channel = bot.get_channel(931567660163006574)
  for i in args:
    info.append(i)
  firstName = info[0]
  lastName = info[1]
  lastnameInitial = lastName[0]
  grade = info[2]
  pl = info[3] 
  nickname = firstName + " " + lastnameInitial + "."
  role = None
  await ctx.message.author.edit(nick = nickname)
  if grade == '7':
    role = ctx.guild.get_role(919285877363077151)
  elif grade == '8':
    role = ctx.guild.get_role(919285664246292531)
  elif grade == '9':
    role = ctx.guild.get_role(919286050365538344)
  elif grade == '10':
    role = ctx.guild.get_role(919286158272376892)
  elif grade == '11':
    role = ctx.guild.get_role(919286222524911636)
  elif grade == '12':
    role = ctx.guild.get_role(919286283996647454)
  await ctx.message.author.add_roles(role)
  await ctx.message.author.send("Info received. Pending verification.")
  verificationMessage = "<@&842892441237323827>" + ' ' + firstName + ' ' + lastName + ', ' + grade + ', ' + pl
  await channel.send(verificationMessage)

@bot.command()
@commands.has_role('Moderator')
async def confirm(ctx, member: discord.Member):
  memberRole = ctx.guild.get_role(838544731792736326)
  outsiderRole = ctx.guild.get_role(838544736464928768)
  await member.add_roles(memberRole)
  await member.remove_roles(outsiderRole)
  await member.send("You have been verified. Welcome!")

@bot.command()
@commands.has_role('Moderator')
async def purge(ctx, number: int):
  await ctx.channel.purge(limit=number)

@bot.command()
    await ctx.send(file=discord.File('doug walker fast clap.gif'))
    
bot.run(token)
  
