import random as r
import discord
from discord.ext import commands

dog_Pic_List = [
    "https://cdn.discordapp.com/attachments/406954453648801794/767162413086408714/Shiba_Inu_1.jpg",
    "https://cdn.discordapp.com/attachments/406954453648801794/767162459210776597/standing_shiba.jpg",
    "https://cdn.discordapp.com/attachments/406954453648801794/767162480312844298/yawning_shiba.jpg",
    "https://cdn.discordapp.com/attachments/406954453648801794/767162545224024094/spring_shiba.jpg",
    "https://cdn.discordapp.com/attachments/406954453648801794/767162572969082920/sleepy_boi.jpg",
    "https://cdn.discordapp.com/attachments/406954453648801794/767260785905893386/good_heart.png",
    "https://cdn.discordapp.com/attachments/406954453648801794/767260789643149323/shiba_pfp_2.jpg",
    "https://cdn.discordapp.com/attachments/406954453648801794/767260792604459028/Charlie_and_the_chocolate_dog.jpg",
    "https://cdn.discordapp.com/attachments/406954453648801794/767260796652093460/cheecks.png",
    "https://cdn.discordapp.com/attachments/406954453648801794/767260803682271242/Floofer_shiba.jpg",
    "https://cdn.discordapp.com/attachments/406954453648801794/767260800465240084/cheeks_2.jpg",
    "https://cdn.discordapp.com/attachments/406954453648801794/767260806353125396/goodest_dog.jpg",
    "https://cdn.discordapp.com/attachments/406954453648801794/767260808974958602/good_looking_boi.jpg"
]

client = commands.Bot(command_prefix= '!')

TOKEN = "Insert Secert Code"

CRINGE_VAR = "https://cdn.discordapp.com/attachments/453079493322473472/739213236037091339/ripsave_-_Mario_had_enough.mp4"

# Says that that bot is ready on bot
@client.event
async def on_ready():
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

# Sends Cringe Video
@client.command()
async def cringe(context):
    await context.send(CRINGE_VAR)

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
