import discord
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client   

    @commands.command(aliases=['p'])
    async def ping(self, ctx):
        await ctx.send('Pong! \n{}ms'.format(round(self.client.latency*1000)))

    @commands.command(aliases=['c'])
    async def clear(self, ctx, amount:int=5):
        try:
            await ctx.channel.purge(limit=(amount+1))
        except:
            await ctx.send('Something went wrong\nTry Again!!')

   
def setup(client):
    client.add_cog(Example(client))