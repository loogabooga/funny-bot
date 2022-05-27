import discord
from discord.ext import commands
import cv2
import requests
from os import remove
import numpy as np

class image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def edge(self, ctx, *, query=""):
        # get image from message attachment
        if ctx.message.attachments:
            url = ctx.message.attachments[0].url
            response = requests.get(url)
            image = cv2.imdecode(np.fromstring(response.content, np.uint8), cv2.IMREAD_COLOR)
        # get image from url
        else:
            url = query
            response = requests.get(url)
            image = cv2.imdecode(np.fromstring(response.content, np.uint8), cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # detect edges
        edges = cv2.Canny(gray, 100, 200)
        # display image
        cv2.imwrite('edge.png', edges)
        # send image
        await ctx.send(file=discord.File('edge.png'))
        # remove image
        remove('edge.png')

def setup(bot):
    bot.add_cog(image(bot))


# if you don't know what the functions mean, just ignore them
# the code is pretty self explanatory
# - Gitbub Copilot
