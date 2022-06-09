import discord
from discord.ext import commands
import rarbgapi
client = rarbgapi.RarbgAPI()

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

class rarbg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def movie(self, ctx, *, query):
        if query == None:
            await ctx.send("Please enter a search query you bitch")
        async with ctx.channel.typing():
            ogaschloga = "```"
            yeah = client.search(search_string=query, categories=[rarbgapi.RarbgAPI.CATEGORY_MOVIE_H264, rarbgapi.RarbgAPI.CATEGORY_MOVIE_H264_1080P, rarbgapi.RarbgAPI.CATEGORY_MOVIE_H264_720P, rarbgapi.RarbgAPI.CATEGORY_MOVIE_H264_4K, rarbgapi.RarbgAPI.CATEGORY_MOVIE_H265_1080P, rarbgapi.RarbgAPI.CATEGORY_MOVIE_H265_4K, rarbgapi.RarbgAPI.CATEGORY_MOVIE_FULL_BD, rarbgapi.RarbgAPI.CATEGORY_MOVIE_BD_REMUX], sort="seeders")
            yeah2 = 0
            for i in yeah:
                if yeah2 == 10:
                    break
                yeah2 += 1
                ogaboga = i.download.replace("magnet:?xt=urn:btih:", "").split("&dn=")[0]
                ogaschloga = ogaschloga + f"{yeah2}. Filename: {i.filename}\nHash: {ogaboga}\n\n"
            ogaschloga = ogaschloga + "```"
        await ctx.send(ogaschloga)

def setup(bot):
    bot.add_cog(rarbg(bot))


# if you don't know what the functions mean, just ignore them
# the code is pretty self explanatory
# - Gitbub Copilot

