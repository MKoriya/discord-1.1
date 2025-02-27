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
        amount += 1
        await ctx.channel.purge(limit=amount)
        await ctx.send('Something went wrong\nTry Again!!')
        print(f'{amount} messages cleared by {ctx.author}.')
            
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.errors.BadArgument):
            print('Clear Error!! didn\'t provided integer')
            await ctx.send('Error! Please enter the Integer ONLY!!')
        else:
            print('Unknown Clear Error!!')
            await ctx.send('Error! Something went wrong\nPlease Try Again!')

   
def setup(client):
    client.add_cog(Example(client))
