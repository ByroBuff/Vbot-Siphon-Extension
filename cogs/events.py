import selfcord as discord
import main
import fade
import platform
import config
from datetime import datetime
from colorama import Fore as F
from selfcord.ext import commands as vbot
from utils import other
from utils.other import log

py_ver = platform.python_version()
bot_ver = main.__version__
siphon_ver = main.__siphon_version__
discord_ver = discord.__version__


def banner(bot):
    extendor = bot.get_user(main.__extendor_id__)
    author = "vined_"
    print(f"""{F.LIGHTBLUE_EX}

           {F.LIGHTMAGENTA_EX}╔═╗╦╔═╗╦ ╦╔═╗╔╗╔
           {F.LIGHTMAGENTA_EX}╚═╗║╠═╝╠═╣║ ║║║║
           {F.LIGHTMAGENTA_EX}╚═╝╩╩  ╩ ╩╚═╝╝╚╝ 
       ╔╗╔╗╔╗╔╗╔╗╔╗╔╗╔╗╔╗╔╗╔╗╔╗
        ╚╝╚╝╚╝╚╝╚╝╚╝╚╝╚╝╚╝╚╝╚╝
            Siphon  v{siphon_ver}""")
    print(f"""
{F.LIGHTBLACK_EX}* {F.LIGHTWHITE_EX}Vbot by {F.LIGHTBLUE_EX}{author}{F.LIGHTBLACK_EX}
{F.LIGHTBLACK_EX}* {F.LIGHTWHITE_EX}Siphon extension by {F.LIGHTMAGENTA_EX}{extendor}{F.LIGHTBLACK_EX}
{F.LIGHTBLACK_EX}* {F.LIGHTBLUE_EX}{len([command for command in bot.walk_commands()])} {F.LIGHTWHITE_EX} total commands and subcommands
{F.LIGHTBLACK_EX}* {F.LIGHTBLUE_EX}93 {F.LIGHTWHITE_EX} original Vbot commands and subcommands
{F.LIGHTBLACK_EX}* {F.LIGHTMAGENTA_EX}{len([command for command in bot.walk_commands()]) - 93} {F.LIGHTWHITE_EX} Siphon extension commands and subcommands
""")


class Events(
        vbot.Cog,
        name="Events"):
    def __init__(self, bot):
        self.bot: vbot.Bot = bot

    @vbot.Cog.listener()
    async def on_connect(self):
        other.clear_console()
        banner(self.bot)
        print(
            f"{F.LIGHTBLACK_EX}Logged in as {F.LIGHTBLUE_EX}{self.bot.user}{F.LIGHTBLACK_EX} with {'prefix ' + F.LIGHTCYAN_EX + main.prefix[0] if len(main.prefix) == 1 else 'prefixes ' + F.LIGHTCYAN_EX + f' {F.LIGHTBLACK_EX}|{F.LIGHTCYAN_EX} '.join(main.prefix)}\n")

        print(f"{F.LIGHTYELLOW_EX}(?){F.LIGHTWHITE_EX} Nitro Sniper enabled: {F.LIGHTRED_EX if config.nitro_sniper == False else F.LIGHTGREEN_EX}{config.nitro_sniper}")
        if config.nitro_sniper:
            print(f"{F.LIGHTGREEN_EX}(+){F.LIGHTWHITE_EX} Nitro sniping {len(self.bot.guilds)} servers")
            
        if config.errorLogging:
            print(f"{F.LIGHTGREEN_EX}(*){F.LIGHTWHITE_EX} Error logging enabled\n")
        else:
            print(f"{F.LIGHTRED_EX}(*){F.LIGHTWHITE_EX} Error logging disabled\n")

    @vbot.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        await self.bot.process_commands(after)

    @vbot.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        if not config.logging:
            return

        log(f"{F.RED}Left server {F.WHITE}| {F.LIGHTBLUE_EX}{guild.name} {F.LIGHTWHITE_EX}({guild.id})")

    @vbot.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        if not config.logging:
            return

        log(f"{F.GREEN}Joined server {F.WHITE}| {F.LIGHTBLUE_EX}{guild.name} {F.LIGHTWHITE_EX}({guild.id})")

    @vbot.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        if not config.logging:
            return

        if member._user == self.bot.user:
            return
          
        log(f"{F.RED}User left a server {F.WHITE}| {F.LIGHTBLUE_EX}{member} - {member.guild.name} {F.LIGHTWHITE_EX}({member.id} - {member.guild.id})")

    @vbot.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if not config.logging:
            return

        if member._user == self.bot.user:
            return
          
        log(f"{F.GREEN}User joined a server {F.WHITE}| {F.LIGHTBLUE_EX}{member} - {member.guild.name} {F.LIGHTWHITE_EX}(User: {member.id} - Server: {member.guild.id})")

    @vbot.Cog.listener()
    async def on_command(self, ctx: vbot.Context):
        if not config.logging:
            return
          
        cmd = ctx.command
        msg = ctx.message
        
        log(f"{F.LIGHTGREEN_EX}[>] {F.LIGHTBLUE_EX}{cmd} {F.LIGHTWHITE_EX}at {f'#{ctx.channel.name}' if not isinstance(ctx.channel, discord.DMChannel) else ctx.channel}")


if __name__ == "__main__":
    print("You need to run main.py to run the bot")


async def setup(bot):
    await bot.add_cog(Events(bot))
