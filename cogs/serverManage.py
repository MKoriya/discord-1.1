import discord
from discord.ext import commands

class ServerManage(commands.Cog):

    def __init__(self, client):
        self.client = client 

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print('{} joined.'.format(member.mention))
        await member.channel.send('Welcome {} Bitch!!'.format(member))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print('{} left.'.format(member))
        await member.channel.send('Bye Bye {} Bitch!!'.format(member))

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} got kicked.')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} got Banned.')

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
                return