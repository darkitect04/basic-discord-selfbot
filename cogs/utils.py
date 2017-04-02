import discord
from discord.ext import commands

class Utils():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kill(self):
        await bot.logout()

    @commands.command(pass_context=True)
    async def getuserid(self, ctx, member : discord.Member):
        await bot.say(member.id)

    @commands.command(pass_context=True)
    async def whatsmyid(self, ctx):
        await bot.say(ctx.author.id)

    @commands.command(pass_context=True)
    async def howmanymembers(self, ctx):
        await bot.say(len(ctx.message.server.members))


def setup(bot):
    bot.add_cog(Utils(bot))
