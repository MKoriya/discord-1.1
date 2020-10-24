import discord
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('Among us'))
        print("We have logged in as a {}".format(self.client.user))

    @commands.command(aliases=['p'])
    async def ping(self, ctx):
        await ctx.send('Pong! \n{}ms'.format(round(self.client.latency*1000)))

    @commands.command(aliases=['c'])
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)

   
def setup(client):
    client.add_cog(Example(client))