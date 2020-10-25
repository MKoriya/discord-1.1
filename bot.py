import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Among us'))
    print("We have logged in as a {}".format(client.user))

@client.command()
async def load(ctx, extension):
    try: 
        client.load_extension(f'cogs.{extension}')
    except:
        await ctx.send("Couldn't load the extension\nPlease Try Again!!")
    else:
        await ctx.send('Seccessfully loaded the {}'.format(extension))
    

@client.command()
async def unload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
    except:
        await ctx.send("Couldn't unload the extension\nPlease Try Again!!")
    else:
        await ctx.send('Seccessfully ulloaded the {}'.format(extension))

@client.command()
async def reload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
    except:
        await ctx.send("Couldn't reload the extension\nPlease Try Again!!")
    else:
        await ctx.send('Seccessfully reloaded the {}'.format(extension))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['DISCORD_TOKEN'])