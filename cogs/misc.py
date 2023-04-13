import selfcord as discord
import random
import main
import config
from colorama import Fore as F
from selfcord.ext import commands as vbot
from utils import other
from utils import alias
from cogs import events
from typing import Optional
import requests
from mcstatus import JavaServer
import re
import datetime
import placeholders


class MiscCmds(
        vbot.Cog,
        name="Misc",
        description="Various miscellanous commands"):
    def __init__(self, bot: vbot.Bot):
        self.bot: vbot.Bot = bot

    @vbot.command(
        name="listening",
        description="Sets your status to Listening"
    )
    async def listening(self, ctx: vbot.Context, *, activity_message: str = "VBot"):
        msg = ctx.message

        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name=activity_message,))

        await msg.edit(content=f"```yaml\n+ Set your listening status to {activity_message}```", delete_after=5)

    @vbot.command(
        name="watching",
        description="Sets your status to Watching"
    )
    async def watching(self, ctx: vbot.Context, *, activity_message: str = "VBot"):
        msg = ctx.message

        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=activity_message))

        await msg.edit(content=f"```yaml\n+ Set your watching status to {activity_message}```", delete_after=5)

    @vbot.command(
        name="playing",
        description="Sets your status to Playing"
    )
    async def playing(self, ctx: vbot.Context, *, activity_message: str = "VBot"):
        msg = ctx.message

        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name=activity_message))

        await msg.edit(content=f"```yaml\n+ Set your playing status to {activity_message}```", delete_after=5)

    @vbot.command(
        name="stopactivity",
        description="Stops your current activity",
        aliases=alias.get_aliases("stopactivity")
    )
    async def stopactivity(self, ctx: vbot.Context):
        await ctx.message.delete()
        await self.bot.change_presence(
            activity=None,
            status=self.bot.status)

    @vbot.group(
        name="status",
        description="Changes your status",
        invoke_without_command=True
    )
    async def status(self, ctx: vbot.Context):
        msg = ctx.message
        await msg.edit(content=f"```yaml\n- Incorrect usage. Correct usage: {ctx.clean_prefix}help [status]```", delete_after=5)

    @status.command(
        name="dnd",
        description="Changes your status to do not disturb"
    )
    async def dnd(self, ctx: vbot.Context):
        msg = ctx.message
        await self.bot.change_presence(status=discord.Status.dnd)
        await msg.edit(content=f"```yaml\nChanged status to do not disturb.```", delete_after=5)

    @status.command(
        name="idle",
        description="Changes your status to idle"
    )
    async def idle(self, ctx: vbot.Context):
        msg = ctx.message
        await self.bot.change_presence(status=discord.Status.idle)
        await msg.edit(content=f"```yaml\nChanged status to idle.```", delete_after=5)

    @status.command(
        name="offline",
        description="Changes your status to offline"
    )
    async def offline(self, ctx: vbot.Context):
        msg = ctx.message
        await self.bot.change_presence(status=discord.Status.invisible)
        await msg.edit(content=f"```yaml\nChanged status to offline```", delete_after=5)

    @status.command(
        name="online",
        description="Changes your status to online"
    )
    async def online(self, ctx: vbot.Context):
        msg = ctx.message
        await self.bot.change_presence(status=discord.Status.online)
        await msg.edit(content=f"```yaml\nChanged status to online.```", delete_after=5)

    @status.command(
        name="none",
        description="Changes your status to none (Gives priority over your discord app status)"
    )
    async def none(self, ctx: vbot.Context):
        msg = ctx.message
        await self.bot.change_presence(status=None)
        await msg.edit(content=f"```yaml\nChanged status to none.```", delete_after=5)

    @vbot.command(
        name="clearconsole",
        description="Clears the console"
    )
    async def clearconsole(self, ctx: vbot.Context):
        await ctx.message.delete()

        other.clear_console()
        events.banner(self.bot)
        print(
            f"{F.LIGHTBLACK_EX}Logged in as {F.LIGHTBLUE_EX}{self.bot.user}{F.LIGHTBLACK_EX} with {'prefix ' + F.LIGHTCYAN_EX + main.prefix[0] if len(main.prefix) == 1 else 'prefixes ' + F.LIGHTCYAN_EX + f' {F.LIGHTBLACK_EX}|{F.LIGHTCYAN_EX} '.join(main.prefix)}\n")

        print(f"{F.LIGHTYELLOW_EX}(?){F.LIGHTWHITE_EX} Nitro Sniper enabled: {F.LIGHTRED_EX if config.nitro_sniper == False else F.LIGHTGREEN_EX}{config.nitro_sniper}")
        if config.nitro_sniper:
            print(
                f"{F.LIGHTGREEN_EX}(+){F.LIGHTWHITE_EX} Nitro sniping {len(self.bot.guilds)} servers\n")

    @vbot.command(
        name="ping",
        description="Sends the bot latency",
        aliases=alias.get_aliases("ping")
    )
    async def ping(self, ctx: vbot.Context):
        msg = ctx.message
        latency = round(self.bot.latency * 1000)

        await msg.edit(content=f"```yaml\nThe bot's latency is {latency}ms```", delete_after=5)

    @vbot.command(
        name="calc",
        description="Calculates a math expression",
    )
    async def calc(self, ctx: vbot.Context, *, expression: str):
        msg = ctx.message
        try:
            e = eval(expression)
            await msg.edit(content=f"```{expression} = {e}" + "```", delete_after=5)
        except:
            await msg.edit(content=f"```yaml\n- Invalid expression```", delete_after=5)

    @vbot.command(
        name="mcstatus",
        description="Gets the status of a minecraft server",
    )
    async def mcstatus(self, ctx: vbot.Context, *, ip: str):
        msg = ctx.message
        await msg.delete()

        try:
            javaServer = JavaServer.lookup(ip)
            status = javaServer.status()
            players = status.players.online
            max_players = status.players.max
            online = "[2;32m🟢ONLINE"
            version = re.sub('§[a-z0-9]', '', status.version.name)

        except ConnectionRefusedError:
            players = 0
            max_players = 0
            online = "[2;31m🔴OFFLINE"
            version = "UNKOWN"

        await ctx.send(f"""
```ansi
[2;36m{ip}
[2;33mPlayers : [2;34m{players}[2;37m/[2;34m{max_players}
[2;33mOnline  : [2;34m{online}
[2;33mversion : [2;34m{version}
```
""", delete_after=5)
        
    @vbot.command(
        name="poll",
        description="Creates a poll",
    )
    async def poll(self, ctx: vbot.Context, *, question: str):
        msg = ctx.message
        await msg.delete()

        newmsg = await ctx.send(f"""
```ansi
[2;30mPoll:[0m
[2;34m{question}
[0m
```
        """)
        await newmsg.add_reaction("👍")
        await newmsg.add_reaction("👎")

    @vbot.command(
        name="chessboard",
        description="Creates a chessboard from a fen string",
    )
    async def chessboard(self, ctx: vbot.Context, *, fen: str):
        msg = ctx.message
        await msg.delete()

        board = requests.get(f"https://fen2image.chessvision.ai/{fen}")
        with open("image.jpg", "wb") as f:
            f.write(board.content)

        await ctx.send(file=discord.File("image.jpg"))
    
    @vbot.command(
            name="placeholder",
            description="commands to replace text in your message"
    )
    async def placeholder(self, ctx: vbot.Context, *, text: str):
        msg = ctx.message

        # Add your own placeholders in placeholders.py
        await msg.edit(placeholders.placeholder(text, ctx))

    @vbot.command(
        name="adlinkbypass",
        description="Bypasses linkvertise links and more"
    )
    async def adlinkbypass(self, ctx: vbot.Context, *, link: str):
        msg = ctx.message

        url = f"https://bypass.pm/bypass2?url={link}"

        bypassed = requests.get(url).json()


        try:
            await msg.edit(f"""
```ansi
[2;31mOriginal link[0m  :  [2;33m{link}[0m
[2;32mBypassed link[0m  :  [2;33m{bypassed['destination']}[0m

```
            """)
        except KeyError:
            await msg.edit(f"""
```ansi
[2;31mOriginal link[0m  :  [2;33m{link}[0m
[2;31mBypassed link[0m  :  [2;33m{bypassed['msg']}[0m

```
""")

    @vbot.command(
        name="instadelete",
        description="Deletes a message immediately"
    )
    async def instadelete(self, ctx: vbot.Context, pause: int, *, message: str):
        msg = ctx.message
        await msg.delete()
        await ctx.send(message, delete_after=pause)
        

if __name__ == "__main__":
    print("You need to run main.py to run the bot")


async def setup(bot):
    await bot.add_cog(MiscCmds(bot))
