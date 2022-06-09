import discord
from discord.ext import commands
import cv2
import requests
from os import remove, system, listdir
import natsort
import numpy as np

class image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command() 
    # send a message to the channel
    async def edge(self, ctx):
        await ctx.send("currently broketn. sorry :(")
    """
    async def edge(self, ctx, *, query=""):
        # get image from message attachment
        if ctx.message.attachments:
            url = ctx.message.attachments[0].url
            if ".png" in url or ".jpg" in url or ".jpeg" in url.lower():
                response = requests.get(url)
                image = cv2.imdecode(np.fromstring(response.content, np.uint8), cv2.IMREAD_COLOR)
                response = requests.get(url)
                image = cv2.imdecode(np.fromstring(response.content, np.uint8), cv2.IMREAD_COLOR)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                # detect edges
                edges = cv2.Canny(gray, 100, 200)
                # display image
                cv2.imwrite('/dev/shm/edge.png', edges)
                # send image
                await ctx.send(file=discord.File('/dev/shm/edge.png'))
            else: 
                fn = ctx.message.attachments[0].filename
                print(fn)
                response = requests.get(url)
                the = open(f"/dev/shm/{fn}", "wb")
                the.write(response.content)
                the.close()
                fps = system(f"ffprobe -v error -select_streams v -of default=noprint_wrappers=1:nokey=1 -show_entries stream=r_frame_rate /dev/shm/{fn}")
                fps = exec(f"{fps}")
                system(f"mkdir /dev/shm/{fn}_frames")
                print(fps)
                system(f"ffmpeg -i /dev/shm/{fn} /dev/shm/{fn}_frames/frame%d.jpg")
                best = natsort.natsorted(listdir(f"/dev/shm/{fn}_frames"))
                print(best)
                for i in best:
                    if ".jpg" in i:
                        img = cv2.imread(f"/dev/shm/{fn}_frames/{i}")
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        edges = cv2.Canny(gray,50,150)
                        cv2.imwrite(f"/dev/shm/{fn}_frames/{i}", edges)
                    else:
                        pass
                system(f"ffmpeg -i /dev/shm/{fn}_frames/frame%d.jpg -r {fps} /dev/shm/{fn}_edges.mp4")
                # take audio from fn to fn_edges
                system(f"ffmpeg -i /dev/shm/{fn}_edges.mp4 -i /dev/shm/{fn} -c copy -map 0:v:0 -map 1:a:0 /dev/shm/{fn}_edge.mp4")
                await ctx.send(file=discord.File(f"/dev/shm/{fn}_edge.mp4"))
                system(f"rm -rf /dev/shm/{fn}_frames")
                system(f"rm -rf /dev/shm/{fn}_edges.mp4")
                system(f"rm -rf /dev/shm/{fn}_edge.mp4")
                system(f"rm -rf /dev/shm/{fn}")
        # get image from url
        else:
            url = query
            if ".png" in url or ".jpg" in url or ".jpeg" in url.lower():
                response = requests.get(url)
                image = cv2.imdecode(np.fromstring(response.content, np.uint8), cv2.IMREAD_COLOR)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                # detect edges
                edges = cv2.Canny(gray, 100, 200)
                # display image
                cv2.imwrite('/dev/shm/edge.png', edges)
                # send image
                await ctx.send(file=discord.File('/dev/shm/edge.png'))
            else:
                await ctx.send("Please attach an image or provide a url to an image.")
                """
def setup(bot):
    bot.add_cog(image(bot))


# if you don't know what the functions mean, just ignore them
# the code is pretty self explanatory
# - Gitbub Copilot
