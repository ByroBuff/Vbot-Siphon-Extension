import selfcord as discord
import random
import base64
import secrets
import string
import aiohttp
import json
import io
import socket
import struct
import main
from colorama import Fore as F
from selfcord.ext import commands as vbot
from utils import alias
import time
import asyncio
import requests
import config
from datetime import datetime
from typing import Optional
import os


class FunCmds(
        vbot.Cog,
        name="Fun",
        description="Various fun commands"):
    def __init__(self, bot):
        self.bot: vbot.Bot = bot
        self.copy_ids = []

    @vbot.group(
        name="copycat",
        description="Copies messages sent by an user.",
        invoke_without_command=True,
        aliases=alias.get_aliases("copycat")
    )
    async def copycat(self, ctx: vbot.Context, user: discord.User):
        msg = ctx.message

        if user.id in self.copy_ids:
            return await msg.edit('```yaml\n- Already copying that user.```', delete_after=5)

        if ctx.message.author.id == user.id:
            return await msg.edit('```yaml\n- You can\'t copy yourself.```', delete_after=5)

        self.copy_ids.append(user.id)
        await msg.edit(content=f"```yaml\n+ Now copying {user}```", delete_after=5)

    @copycat.command(
        name="reset",
        description="Resets copycat"
    )
    async def reset(self, ctx: vbot.Context):
        self.copy_ids = []
        await ctx.message.edit(content='```yaml\n+ Succesfully reset copycat list.```', delete_after=5)

    @vbot.command(
        name="someone",
        description="Pings a random person in a server (if it doesn't work don't blame me)"
    )
    async def someone(self, ctx: vbot.Context):
        msg = ctx.message
        guild = ctx.guild
        members = [member.mention for member in guild.members]

        await msg.edit(content=secrets.choice(members))

    @vbot.command(
        name="stealpfp",
        description="Steals someones pfp (after 2 - 3 pfps there will be a ratelimit)",
        aliases=alias.get_aliases("stealpfp")
    )
    async def stealpfp(self, ctx: vbot.Context, member: discord.User):
        msg = ctx.message
        

        avatar_url = str(member.avatar.url)

        img = requests.get(avatar_url)
        img = img.content

        await self.bot.user.edit(avatar=img)
        await msg.edit(content=f"```yaml\n+ Succesfully set pfp to {member}'s profile picture```", delete_after=5)

    @vbot.command(
        name="tokengrab",
        description="ACTUALLY token grabs someone. Do not use this in public!!",
    )
    async def tokengrab(self, ctx: vbot.Context, member: discord.User):
        with open("./fun/tokens.json") as json_f:
            data = json.load(json_f)

        msg = ctx.message
        mid = str(member.id)

        if mid not in data:
            id_ascii = mid.encode('ascii')
            id_base64 = base64.b64encode(id_ascii)
            id_idk = id_base64.decode('ascii')
            timest = ''.join(random.choices(
                string.ascii_letters + string.digits + "-" + "_", k=6))
            last = ''.join(random.choices(
                string.ascii_letters + string.digits + "-" + "_", k=27))
            await msg.edit(content=f"```yaml\n+ Succesfully token grabbed {member}.\nToken: {id_idk}.{timest}.{last}```")
            data[mid] = f"{id_idk}.{timest}.{last}"

            with open("./fun/tokens.json", "w") as out:
                json.dump(data, out, indent=4)

        else:
            token = data[mid]
            await msg.edit(content=f"```yaml\n+ Succesfully token grabbed {member}.\nToken: {token}```")

    @vbot.command(
        name="ip",
        description="ACTUALLY ip grabs someone. Do not use this in public!!",
        aliases=alias.get_aliases("ip")
    )
    async def ip(self, ctx: vbot.Context, member: discord.User):
        with open("./fun/ips.json") as json_f:
            data = json.load(json_f)

        msg = ctx.message
        mid = str(member.id)

        if mid not in data:
            rand_ip = socket.inet_ntoa(struct.pack(
                '>I', random.randint(1, 0xffffffff)))
            await msg.edit(content=f"```yaml\n+ Succesfully IP grabbed {member}.\nIP Address: {rand_ip}```")
            data[mid] = rand_ip

            with open("./fun/ips.json", "w") as out:
                json.dump(data, out, indent=4)

        else:
            ip = data[mid]
            await msg.edit(content=f"```yaml\n+ Succesfully IP grabbed {member}.\nIP Address: {ip}```")

    @vbot.group(
        name="gen",
        description="Various commands to generate fake info",
        aliases=alias.get_aliases("gen"),
        invoke_without_command=True
    )
    async def gen(self, ctx: vbot.Context):
        await ctx.message.delete()

    @gen.command(
        name="tokens",
        description="Generates tokens"
    )
    async def tokens(self, ctx: vbot.Context, amount: int = 20):
        msg = ctx.message
        tokens = []

        for _ in range(amount):
            id_ascii = str(secrets.choice(
                range(650000000000000000, 1200000000000000000))).encode('ascii')
            id_base64 = base64.b64encode(id_ascii)
            id_idk = id_base64.decode('ascii')
            timest = ''.join(random.choices(
                string.ascii_letters + string.digits + "-" + "_", k=6))
            last = ''.join(random.choices(
                string.ascii_letters + string.digits + "-" + "_", k=27))
            token = f"{id_idk}.{timest}.{last}"
            tokens.append(token)

        nl = "\n"
        fullstr = f"""Generated {amount} tokens
{nl.join(tokens)}"""
        if len(fullstr) > 1998:
            await msg.edit(content="```yaml\nMaking txt file...```")
            f = io.StringIO(fullstr)
            await ctx.send(file=discord.File(f, filename="tokens.txt"))
            await msg.delete()

        else:
            await msg.edit(content=f"""```yaml
Generated {amount} tokens
{nl.join(tokens)}```""")

    @gen.command(
        name="ips",
        description="Generates IPs"
    )
    async def ips(self, ctx: vbot.Context, amount: int = 20):
        msg = ctx.message
        ips = []

        for _ in range(amount):
            ip = socket.inet_ntoa(struct.pack(
                '>I', random.randint(1, 0xffffffff)))
            ips.append(str(ip))

        nl = "\n"
        fullstr = f"""Generated {amount} IPs
{nl.join(ips)}"""
        if len(fullstr) > 1998:
            await msg.edit(content="```yaml\nMaking txt file...```")
            f = io.StringIO(fullstr)
            await ctx.send(file=discord.File(f, filename="ips.txt"))
            await msg.delete()

        else:
            await msg.edit(content=f"""```yaml
Generated {amount} IPs
{nl.join(ips)}```""")

    @gen.command(
        name="ids",
        description="Generates Discord IDs"
    )
    async def ids(self, ctx: vbot.Context, amount: int = 20):
        msg = ctx.message
        ids = []

        for _ in range(amount):
            id = str(secrets.choice(
                range(100000000000000000, 1200000000000000000)))
            ids.append(id)

        nl = "\n"
        fullstr = f"""Generated {amount} IDs
{nl.join(ids)}"""
        if len(fullstr) > 1998:
            await msg.edit(content="```yaml\nMaking txt file...```")
            f = io.StringIO(fullstr)
            await ctx.send(file=discord.File(f, filename="ids.txt"))
            await msg.delete()

        else:
            await msg.edit(content=f"""```yaml
Generated {amount} IDs
{nl.join(ids)}```""")

    @gen.command(
        name="nitro",
        description="Generates Discord nitro codes"
    )
    async def nitro(self, ctx: vbot.Context, amount: int = 20):
        msg = ctx.message
        codes = []

        for _ in range(amount):
            code = ''.join(random.choices(
                string.ascii_letters + string.digits, k=16))
            codes.append(f'https://discord.gift/{code}')

        nl = "\n"
        fullstr = f"""Generated {amount} nitro code(s)
{nl.join(codes)}"""
        if len(fullstr) > 1998:
            await msg.edit(content="```yaml\nMaking txt file...```")
            f = io.StringIO(fullstr)
            await ctx.send(file=discord.File(f, filename="nitro_codes.txt"))
            await msg.delete()

        else:
            await msg.edit(content=f"""```yaml
Generated {amount} nitro code(s)
{nl.join(codes)}```""")

    @vbot.command(
        name="firstmsg",
        description="Sends the first message in the current channel"
    )
    async def firstmsg(self, ctx: vbot.Context):
        msg = ctx.message

        history = [message async for message in ctx.message.channel.history(oldest_first=True)]
        firstm = history[0]
        print(firstm.content)
        print(firstm.author.name + "#" + history[0].author.discriminator)
        await msg.edit(content=f"""```yaml
From: {firstm.author}
Message: {firstm.content.strip("```")}

```link: {firstm.jump_url}""")

    @vbot.group(
        name="fact",
        description="A bunch of animal facts",
        invoke_without_command=True
    )
    async def facts(self, ctx: vbot.Context):
        msg = ctx.message
        await msg.edit(content=f"```yaml\n- Incorrect usage. Correct usage: {ctx.clean_prefix}help [facts]```", delete_after=5)

    @facts.command(
        name="bird",
        description="Random bird fact"
    )
    async def bird(self, ctx: vbot.Context):
        msg = ctx.message

        async with aiohttp.ClientSession() as http:
            r = await http.get(f"https://some-random-api.ml/animal/bird")
            js = await r.json()
            fact = js["fact"]
            image = js["image"]
            await ctx.send(f"""```yaml\nBird Fact: {fact}```\n{image}""")

        await msg.delete(delay=5)

    @facts.command(
        name="cat",
        description="Random cat fact"
    )
    async def cat(self, ctx: vbot.Context):
        msg = ctx.message

        async with aiohttp.ClientSession() as http:
            r = await http.get(f"https://some-random-api.ml/animal/cat")
            js = await r.json()
            fact = js["fact"]
            image = js["image"]
            await ctx.send(f"""```yaml\nCat Fact: {fact}```\n{image}""")

        await msg.delete(delay=5)

    @facts.command(
        name="dog",
        description="Random dog fact"
    )
    async def dog(self, ctx: vbot.Context):
        msg = ctx.message

        async with aiohttp.ClientSession() as http:
            r = await http.get(f"https://some-random-api.ml/animal/dog")
            js = await r.json()
            fact = js["fact"]
            image = js["image"]
            await ctx.send(f"""```yaml\nDog Fact: {fact}```\n{image}""")

        await msg.delete(delay=5)

    @facts.command(
        name="kangaroo",
        description="Random kangaroo fact"
    )
    async def kangaroo(self, ctx: vbot.Context):
        msg = ctx.message

        async with aiohttp.ClientSession() as http:
            r = await http.get(f"https://some-random-api.ml/animal/kangaroo")
            js = await r.json()
            fact = js["fact"]
            image = js["image"]
            await ctx.send(f"""```yaml\nKangaroo Fact: {fact}```\n{image}""")

        await msg.delete(delay=5)

    @facts.command(
        name="raccoon",
        description="Random raccoon fact"
    )
    async def raccoon(self, ctx: vbot.Context):
        msg = ctx.message

        async with aiohttp.ClientSession() as http:
            r = await http.get(f"https://some-random-api.ml/animal/raccoon")
            js = await r.json()
            fact = js["fact"]
            image = js["image"]
            await ctx.send(f"""```yaml\nRaccoon Fact: {fact}```\n{image}""")

        await msg.delete(delay=5)

    @facts.command(
        name="panda",
        description="Random panda fact"
    )
    async def panda(self, ctx: vbot.Context):
        msg = ctx.message

        async with aiohttp.ClientSession() as http:
            r = await http.get(f"https://some-random-api.ml/animal/panda")
            js = await r.json()
            fact = js["fact"]
            image = js["image"]
            await ctx.send(f"""```yaml\nPanda Fact: {fact}```\n{image}""")

        await msg.delete(delay=5)

    @facts.command(
        name="fox",
        description="Random fox fact"
    )
    async def fox(self, ctx: vbot.Context):
        msg = ctx.message

        async with aiohttp.ClientSession() as http:
            r = await http.get(f"https://some-random-api.ml/animal/fox")
            js = await r.json()
            fact = js["fact"]
            image = js["image"]
            await ctx.send(f"""```yaml\nFox Fact: {fact}```\n{image}""")

        await msg.delete(delay=5)

    @facts.command(
        name="koala",
        description="Random koala fact"
    )
    async def koala(self, ctx: vbot.Context):
        msg = ctx.message

        async with aiohttp.ClientSession() as http:
            r = await http.get(f"https://some-random-api.ml/animal/koala")
            js = await r.json()
            fact = js["fact"]
            image = js["image"]
            await ctx.send(f"""```yaml\nKoala Fact: {fact}```\n{image}""")

        await msg.delete(delay=5)

    @facts.command(
        name="redpanda",
        description="Random red panda fact"
    )
    async def redpanda(self, ctx: vbot.Context):
        msg = ctx.message

        async with aiohttp.ClientSession() as http:
            r = await http.get(f"https://some-random-api.ml/animal/red_panda")
            js = await r.json()
            fact = js["fact"]
            image = js["image"]
            await ctx.send(f"""```yaml\nRed Panda Fact: {fact}```\n{image}""")

        await msg.delete(delay=5)

    @vbot.group(
            name="animate",
            description="constantly edits a message so it looks animated"
    )
    async def animate(self, ctx: vbot.Context):
        pass

    @animate.command(
            name="extend",
            description="default animation"
    )
    async def extend(self, ctx: vbot.Context, *, text: str="ByroBuff on top"):
        msg = ctx.message
        await msg.add_reaction("❌")
        self.is_animating = True

        while self.is_animating:
            for i in range(len(text)):
                await msg.edit(content=f"```{text[:i+1]}```")
                time.sleep(0.1)

                if i == len(text) - 1:
                    time.sleep(1)

    @animate.command(
            name="shift",
            description="shifts the text from left to right and back"
    )
    async def shift(self, ctx: vbot.Context, spacing=1, counter=5, *, text: str="ByroBuff on top"):
        msg = ctx.message
        await msg.add_reaction("❌")
        self.is_animating = True

        while self.is_animating:
            for i in range(counter):
                await msg.edit(content=f"```{' '*spacing*i}{text}```")
                time.sleep(0.1)

            for i in range(counter, 0, -1):
                await msg.edit(content=f"```{' '*spacing*i}{text}```")
                time.sleep(0.1)

    @animate.command(
            name="custom",
            description="custom animation"
    )
    async def custom(self, ctx: vbot.Context, *, animation : Optional[str] = None):

        msg = ctx.message

        animDir = os.getcwd() + "\\animations"
        animationFiles = os.listdir(animDir)
        animations = []
        for animationFile in animationFiles:
            if animationFile.endswith(".txt"):
                animations.append(animationFile[:-4])

        if animation is None:
            animationList = ""
            for animation in animations:
                animationList += f"- '{animation}'\n"

            await ctx.send(f"""```yaml\nAnimations:\n{animationList}```""")

        else:
            if animation in animations:
                with open(animDir + f"\\{animation}.txt", "r") as f:
                    if (len(f.read()) == 0):
                        await msg.edit(f"```yaml\nAnimation '{animation}' is empty```", delete_after=5)
                        return
                await msg.add_reaction("❌")
                self.is_animating = True
                while self.is_animating:
                    with open(animDir + f"\\{animation}.txt", "r") as f:
                        for line in f:
                            await msg.edit(line)
                            time.sleep(0.1)
            else:
                await msg.edit(f"```yaml\nAnimation '{animation}' not found```")
       

    @animate.command(
            name="bounce",
            description="bounces the text up and down"
    )
    async def bounce(self, ctx: vbot.Context, lines=5, *, text: str="ByroBuff on top"):
        msg = ctx.message
        await msg.add_reaction("❌")
        self.is_animating = True

        while self.is_animating:
            for i in range(lines):
                await msg.edit(content="```" + "\n​"*i + text + "```")
                time.sleep(0.1)

            for i in range(lines, 0, -1):
                await msg.edit(content="```" + "\n​"*i + text + "```")
                time.sleep(0.1)


    @vbot.command(
            name="ghostping",
            description="ghostpings a user in every channel in the server"
    )
    async def ghostping(self, ctx: vbot.Context, user: discord.User):
        msg = ctx.message
        await msg.delete()
        for channel in ctx.guild.channels:
            if isinstance(channel, discord.TextChannel):
                try:
                    lol = await channel.send(user.mention)
                    await lol.delete()

                except discord.HTTPException:
                    pass

                except discord.MissingPermissions:
                    pass

    @vbot.command(
            name="wasted",
            description="Wasted overlay on avatar"
    )
    async def wasted(self, ctx: vbot.Context, user: discord.User=None):

        msg = ctx.message
        await msg.delete()

        avatar_url = str(user.avatar.url)

        r = requests.get(f"https://some-random-api.ml/canvas/wasted?avatar={avatar_url}")

        with open("image.jpg", "wb") as f:
            f.write(r.content)

        await ctx.send(file=discord.File("image.jpg"))  

    @vbot.command(
            name="cock",
            description="Generates a cock description for a user"
    )
    async def cock(self, ctx: vbot.Context, user: discord.User=None):
        msg = ctx.message

        size = random.randint(1, 9)
        girth = round(random.uniform(1, 2), 2)
        color = random.choice(["✊🏿", "✊🏾", "✊🏽", "✊🏼", "✊🏻"])
        curve = random.choice(["none", "slighty to the left", "strongly to left", "slightly to the right", "strongly to the right", "slightly up", "strongly up" , "slightly down", "strongly down"])
        if girth <= 1.3:
            char = "-"
        else:
            char="="
        representation = "8" + char*size + "D"

        message = f"""
```ansi
[2;36m{user.name}'s cock[0m

[2;34mSize [0m: [2;33m{size}[0m in
[2;34mGirth[0m : [2;33m{girth}[0m in
[2;34mColor [0m: [2;33m{color}[0m
[2;34mCurve [0m: [2;33m{curve}[0m
[2;31mFinal Result[0m:
{representation}
```
        """

        await msg.edit(content=message)

    @vbot.command(
            name="inspire",
            description="Sends an inspirational quote as if you said it"
    )
    async def inspire(self, ctx: vbot.Context):
        msg = ctx.message
        await msg.delete()

        quote = requests.get(f"https://api.themotivate365.com/stoic-quote").json()["quote"]
        await ctx.send(content=quote)

    @vbot.command(
            name="twerk",
            description="Twerks on a random person"
    )
    # Suggested by the faggot 28st
    async def twerk(self, ctx: vbot.Context):
        msg = ctx.message
        await msg.edit(content=f"{self.bot.user.mention} just twerked on {random.choice(ctx.guild.members).mention} 🥵:interrobang:")

    @vbot.command(
            name="slotmachine",
            description="Slot machine"
    )
    async def slotmachine(self, ctx: vbot.Context):

        msg = ctx.message
        items = ["🍇", "🍒", "🍋"]

        timings = [0, 0, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.4, 0.4, 0.4, 1.2, 1.2, 2]

        for timing in timings:
            await msg.edit(content=f"`[{random.choice(items)}|{random.choice(items)}|{random.choice(items)}]`")
            time.sleep(timing)

        finalOne = random.choice(items)
        finalTwo = random.choice(items)
        finalThree = random.choice(items)
        await msg.edit(content=f"`[{finalOne}|{finalTwo}|{finalThree}]`", delete_after=10)

        if finalOne == finalTwo == finalThree:
            await ctx.send(f"`You won the jackpot! 🎉🥇`", delete_after=5)
        elif finalOne == finalTwo or finalOne == finalThree or finalTwo == finalThree:
            await ctx.send(f"`You won! 🎉`", delete_after=10)
        else:
            await ctx.send(f"`You lost! 😔`", delete_after=10)

    @vbot.command(
            name="coinflip",
            description="Flips a coin"
    )
    async def coinflip(self, ctx: vbot.Context):
        msg = ctx.message
        await msg.delete()

        await ctx.send(f"`Its {random.choice(['Heads 😊', 'Tails 🐒'])}!`", delete_after=10)

    @vbot.command(
            name="gaymeter",
            description="Shows how gay a person is"
    )
    async def gaymeter(self, ctx: vbot.Context, user: discord.User=None):
        percent = random.randint(0, 100)
        msg = ctx.message
        await msg.edit(f"{user.mention} `is {percent}% gay 🏳️‍🌈`", delete_after=10)

    @vbot.command(
            name="wyr",
            description="Would you rather"
    )
    async def wyr(self, ctx: vbot.Context, *, question: str):
        msg = ctx.message
        await msg.delete()

        option1 = question[:question.find("or")]
        option2 = question[question.find("or")+3:]

        msg = await ctx.send(f"```yaml\nWould you rather:\n\n1️⃣ - {option1}\n2️⃣ - {option2}```")
        await msg.add_reaction(str("1️⃣"))
        await msg.add_reaction(str("2️⃣"))

    @vbot.command(
            name="empty",
            description="Sends an empty message"
    )
    async def empty(self, ctx: vbot.Context):
        msg = ctx.message
        await msg.delete()

        await ctx.send("​")

    @vbot.Cog.listener()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        if int(payload.user_id) == int(self.bot.user.id) and payload.emoji.name == "❌":
            self.is_animating = False

            print(f"{F.GREEN}[+]{F.LIGHTWHITE_EX} Stopped animating.")
            channel = self.bot.get_channel(payload.channel_id)
            msg = await channel.fetch_message(payload.message_id)

            await asyncio.sleep(1)
            await msg.delete()



    @vbot.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.id in self.copy_ids:
            if message.content.startswith(tuple(main.prefix)):
                return
            else:
                await message.channel.send(message.content)


if __name__ == "__main__":
    print("You need to run main.py to run the bot")


async def setup(bot):
    await bot.add_cog(FunCmds(bot))
