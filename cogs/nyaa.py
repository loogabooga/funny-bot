import discord
from discord.ext import commands
import NyaaPy.nyaa as Nyaa

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

def sort(List):
    List = list(List)
    x = 0
    for i in range(len(List)):
        y = dict(List[i])
        y = int(y["seeders"])
        if y > x:
            x = y
            print(f"x: {x}, y: {y}")
            List.insert(0, List.pop(i))

    return List

class nyaa(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def nyaa(self, ctx, *, query):
        result = Nyaa.Nyaa.search(keyword=query,category=1)
        result = sort(result)
        name = "```"
        for i in range(10):
            try:
                name = name + f"{i+1}. {str(result[i]['name'])}\nHash: {Nyaa.Nyaa.get(result[i]['id'])['hash']}\nSeeders: {str(result[i]['seeders'])}\n\n"
            except:
                pass
        name = name + "```"
        await ctx.send(name)
    @commands.command()
    async def hash(self, ctx, *, id):
        result = Nyaa.Nyaa.get(id)
        await ctx.send(result["hash"])


def setup(bot):
    bot.add_cog(nyaa(bot))