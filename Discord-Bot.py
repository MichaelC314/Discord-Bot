import random as r
import discord
from discord.ext import commands

'''
// Outdated
dog_Pic_List = []
'''

client = commands.Bot(command_prefix= '!')

TOKEN = "Insert Secert Code"

# Says that that bot is ready on bot
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Am Doggo Bot))
    print("Bot is Ready")
     
# Sends pics of doggos
@client.command()
async def doggo(context):
    await context.send(r.choice(dog_Pic_List))

# Sends Bark!
@client.command()
async def bark(context):
    await context.send('Bark!')

# Sends Bork!
@client.command()
async def bork(context):
    await context.send('Bork!')

############################### Dices Below ###############################

# d20
@client.command()
async def d20(context):
    await context.send(r.randint(1,20))

# d12
@client.command()
async def d12(context):
    await context.send(r.randint(1,12))

# d10
@client.command()
async def d10(context):
    await context.send(r.randint(1,10))

# d8
@client.command()
async def d8(context):
    await context.send(r.randint(1,8))

# d6
@client.command()
async def d6(context):
    await context.send(r.randint(1,6))

# d4
@client.command()
async def d4(context):
    await context.send(r.randint(1,4))

############################### Dices Above ###############################

# Clears messages and bot says First!
@client.command()
@commands.has_role("Owner")
async def first(context, mil=1_000_000):
    await context.channel.purge(limit=mil)
    await context.send("First!")

# Clears set amount of messages, standard is 10
@client.command()
@commands.has_role("Owner")
async def clear(context, amount=10):
    await context.channel.purge(limit=amount + 1)


# Runs the bot
client.run(TOKEN)
