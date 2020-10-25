import discord
from discord.ext import commands

class ServerManage(commands.Cog):

    def __init__(self, client):
        self.client = client 

    # @commands.Cog.listener()
    # async def on_member_join(self, member):
    #     print('{} joined.'.format(member.mention))
    #     await member.channel.send('Welcome {} Bitch!!'.format(member))

    # @commands.Cog.listener()
    # async def on_member_remove(self, member):
    #     print('{} left.'.format(member))
    #     await member.channel.send('Bye Bye {} Bitch!!'.format(member))

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} got kicked.')
        print(f'{member.name}#{member.discriminator} got kicked. by {ctx.author}')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have permission to kick members!')
            print('Kick Error! Try to kick without Permission')
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Requsted Member is not in Server\nPlease Try Again!!')
            print('Kick Error! Member is not in Server')
        else:
            await ctx.send('Something went wrong\nPlease Try Again Later')
            print('Unknown Kick Error!!')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} got Banned.')
        print(f'{member.name}#{member.discriminator} got banned')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have permission to ban members!')
            print('Ban Error! Try to ban without Permission')
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Requsted Member is not in Server\nPlease Try Again!!')
            print('Ban Error! Member is not in Server')
        else:
            await ctx.send('Something went wrong\nPlease Try Again Later')
            print('Unknown Ban Error!!')          

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')   
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                print(f'{user.name}#{user.discriminator} unbanned.')
                return

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have permission to ban members!')
            print('Unban Error! Don\'t have permission')
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Member not found\nPlease Try Again!!')
            print('Unban Error! Member not found')
        else:
            await ctx.send('Something went wrong\nPlease Try Again Later')
            print('Unknown Unban Error!!')

def setup(client):
    client.add_cog(ServerManage(client))
