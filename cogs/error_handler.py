import traceback
import sys
from selfcord.ext import commands as vbot
import config
from colorama import Fore as F
from utils.other import log


class ErrorHandler(vbot.Cog):
    def __init__(self, bot):
        self.bot: vbot.Bot = bot
    if config.errorLogging == "channel":
        @vbot.Cog.listener()
        async def on_command_error(self, ctx: vbot.Context, error):
            cog = ctx.cog
            msg = ctx.message

            if cog:
                if cog._get_overridden_method(cog.cog_command_error) is not None:
                    return

            error = getattr(error, 'original', error)

            if isinstance(error, vbot.CommandNotFound):
                await msg.edit(content=f"```yaml\n❌ The command \"{msg.content.split(' ')[0]}\" does not exist.```", delete_after=5)

            elif isinstance(error, vbot.MissingRequiredArgument):
                await msg.edit(content=f"```yaml\n❌ You forgot to write the parameter \"{error.param.name}\".```", delete_after=5)

            elif isinstance(error, vbot.BadArgument):
                await msg.edit(content=f"```yaml\n❌ You entered a parameter incorrectly.```", delete_after=5)

            elif isinstance(error, vbot.MissingPermissions):
                await msg.edit(content=f"```yaml\n❌ You don't have enough permissions to perform this command.```", delete_after=5)

            elif isinstance(error, Exception):
                await msg.edit(content=f"```yaml\n❌ An unknown error occurred: {error}```", delete_after=5)

            else:
                print('Ignoring exception in command {}:'.format(
                    ctx.command), file=sys.stderr)
                traceback.print_exception(
                    type(error), error, error.__traceback__, file=sys.stderr)
                
    elif config.errorLogging == "console":
        @vbot.Cog.listener()
        async def on_command_error(self, ctx: vbot.Context, error):
            cog = ctx.cog
            msg = ctx.message

            if cog:
                if cog._get_overridden_method(cog.cog_command_error) is not None:
                    return

            error = getattr(error, 'original', error)

            if isinstance(error, vbot.CommandNotFound):
                log(f"{F.LIGHTRED_EX}[!] {F.WHITE}The command {F.LIGHTBLUE_EX}\"{msg.content.split(' ')[0]}\"{F.WHITE} does not exist{F.RESET}")
                await msg.delete()

            elif isinstance(error, vbot.MissingRequiredArgument):
                log(f"{F.LIGHTRED_EX}[!] {F.WHITE}You forgot to write the parameter {F.LIGHTBLUE_EX}\"{error.param.name}\"{F.RESET}")
                await msg.delete()

            elif isinstance(error, vbot.BadArgument):
                log(f"{F.LIGHTRED_EX}[!] {F.WHITE}You entered a parameter incorrectly.{F.RESET}")
                await msg.delete()

            elif isinstance(error, vbot.MissingPermissions):
                log(f"{F.LIGHTRED_EX}[!] {F.WHITE}You don't have enough permissions to perform this command. {F.RESET}")
                await msg.delete()

            elif isinstance(error, Exception):
                log(f"{F.LIGHTRED_EX}[!] {F.WHITE}An unknown error occured: {F.LIGHTBLUE_EX}{error}{F.RESET}")
                await msg.delete()

            else:
                log('Ignoring exception in command {}:'.format(
                    ctx.command), file=sys.stderr)
                traceback.print_exception(
                    type(error), error, error.__traceback__, file=sys.stderr)
                
    else:
        @vbot.Cog.listener()
        async def on_command_error(self, ctx: vbot.Context, error):
            cog = ctx.cog
            msg = ctx.message

            msg.delete()



async def setup(bot):
    await bot.add_cog(ErrorHandler(bot))
