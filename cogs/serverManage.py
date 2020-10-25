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
        try: 
            await member.kick(reason=reason)
        except(commands.MemberNotFound):
            print('Member Not Found')
            await ctx.send('Requested Member not Found\nPlease Try Again!!')
        except(commands.MissingPermissions):
            await ctx.send('You don\'t have permission to kick members')
        except:
            await ctx.send('Something went wrong\nPlease Try Again Later')
        else:
            await ctx.send(f'{member.mention} got kicked.')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        try:
            await member.ban(reason=reason)    
        except(commands.MemberNotFound):
            print('Member Not Found')
            await ctx.send('Requested Member not Found\nPlease Try Again!!')
        except(commands.MissingPermissions):
            await ctx.send('You don\'t have permission to kick members')
        except:
            await ctx.send('Something went wrong\nPlease Try Again Later')
        else:
            await ctx.send(f'{member.mention} got Banned.')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        try:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')   
            for ban_entry in banned_users:
                user = ban_entry.user
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f'Unbanned {user.mention}')
                    return
        except(commands.MemberNotFound):
            print('Member Not Found')
            await ctx.send('Requested Member not Found\nPlease Try Again!!')
        except(commands.MissingPermissions):
            await ctx.send('You don\'t have permission to kick members')
        except:
            await ctx.send('Something went wrong\nPlease Try Again Later')


def setup(client):
    client.add_cog(ServerManage(client))