import base64
from art import text2art
from selfcord.ext import commands as vbot
from deep_translator import GoogleTranslator


class TextCmds(
        vbot.Cog,
        name="Text",
        description="Various commands for text editing"):
    def __init__(self, bot):
        self.bot: vbot.Bot = bot

    @vbot.command(
        name="encode",
        description="Encodes a string into base64"
    )
    async def encode(self, ctx, *, string):
        msg = ctx.message

        message_bytes = string.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        await msg.edit(content=f"```yaml\n{base64_message}```")

    @vbot.command(
        name='decode',
        description="Decodes a base64 string (or any string)"
    )
    async def decode(self, ctx, *, string):
        msg = ctx.message

        base64_bytes = string.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')

        await msg.edit(content=f"```yaml\n{message}```")

    @vbot.command(
        name="space",
        description="Spaces every character in a string"
    )
    async def space(self, ctx, *, txt):
        msg = ctx.message
        spaced_txt = " ".join([''.join(item) for item in zip(txt[::1])])

        try:
            await msg.edit(content=spaced_txt)

        except Exception as e:
            await msg.edit(content=f"```yaml\n- An error has occurred: {e}")

    @vbot.command(
        name="upper",
        description="Makes every character uppercase in a string"
    )
    async def _upper(self, ctx, *, txt):
        msg = ctx.message
        uppercased = txt.upper()

        try:
            await msg.edit(content=uppercased)

        except Exception as e:
            await msg.edit(content=f"```yaml\n- An error has occurred: {e}")

    @vbot.command(
        name="lower",
        description="Makes every character lowercase in a string"
    )
    async def _lower(self, ctx, *, txt):
        msg = ctx.message
        lowercased = txt.lower()

        try:
            await msg.edit(content=lowercased)

        except Exception as e:
            await msg.edit(content=f"```yaml\n- An error has occurred: {e}")

    @vbot.command(
        name="invert",
        description="Inverts the characters' case (use command to understand)"
    )
    async def invert(self, ctx, *, txt):
        msg = ctx.message
        inverted = txt.swapcase()

        try:
            await msg.edit(content=inverted)

        except Exception as e:
            await msg.edit(content=f"```yaml\n- An error has occurred: {e}")

    @vbot.command(
        name="reverse",
        description="Reverses a string"
    )
    async def reverse(self, ctx, *, txt):
        msg = ctx.message
        reversed = txt[::-1]

        try:
            await msg.edit(content=reversed)

        except Exception as e:
            await msg.edit(content=f"```yaml\n- An error has occurred: {e}")

    @vbot.command(
        name="annoy",
        description="Makes a string annoying"
    )
    async def annoy(self, ctx, *, txt):
        msg = ctx.message
        annoying = ""

        for idx in range(len(txt)):
            if not idx % 2:
                annoying += txt[idx].upper()

            else:
                annoying += txt[idx].lower()

        await msg.edit(content=annoying)

    @vbot.group(
        name="ascii",
        description="ASCII-ify your message",
        invoke_without_command=True
    )
    async def ascii(self, ctx: vbot.Context, *, message: str):
        msg = ctx.message
        text = text2art(message)
        await msg.edit(content=f'```yaml\n{text}```')

    @ascii.command(
        name="random",
        description="ASCII-ify your message with a random font"
    )
    async def asciirandom(self, ctx: vbot.Context, *, message: str):
        msg = ctx.message
        try:
            text = text2art(message, font="random")
            await msg.edit(content=f'```yaml\n{text}```')

        except Exception as e:
            await msg.edit(content=f"```yaml\n- An error has occurred: {e}")

    @vbot.command(
        name="fancy",
        description="Makes your message fancy"
    )
    async def fancy(self, ctx, *, txt):
        msg = ctx.message
        normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        fancy = "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟"
        fancy_txt = txt.maketrans(normal, fancy)

        await msg.edit(content=txt.translate(fancy_txt))

    @vbot.command(
        name="cursed",
        description="Makes your message look cursed"
    )
    async def cursed(self, ctx, *, txt):
        msg = ctx.message
        normal = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        cursed = ["A̴̻͖̐͜͠","B̸̘̠͖̈́̒͘","C̵̡͓̠̿͒͝","D̴̢̼͔͒̓̚","E̴̙̠̝̔́͝","F̸̢͉͖̐͌̿","G̸͚͖̻͐̔͝","H̸̘̠͒̔̚͜","I̸̢͍͕͌͑͠","J̸͚̺̦̈́͋","K̵͇̓͜͠͝","L̵̪͚͓̽͆͠","M̴̢͎͔̔̾͝","N̸̺͓͙̿̈́̈́","O̸̘̞͉̓͊̚","P̸̡̢̞̿̓","Q̵͕̟͎́͒̚","R̴͖̪̟͐͘͝","Ś̵̫̟̔̕","T̴͍͙̺̀̔̕","U̵͍͚͑͒͝","V̵̘͚͎̿́͊","W̴͕̠͋͊̿","X̴̢̘̙̿͆̚","Y̴̢̪̞̐̾͑","Z̸̙̪̦͘͝͝","a̴͉͔̔̈́͜͝","b̸͇̟̞͊͑͠","c̸̟̺͎͆́̓","d̵͎͇̺̿̐̈́","e̴͕̦̼̒̕͝","f̸͕͍͆͑͝","g̸͓͙͍̀̈́͝","h̵̢̙̀͝͝","i̴̙̼͕͑̾͝","j̴̢̫̺̐͐͘","k̸̫̟̀͌͠","ĺ̵̢̼̟̚͝","m̸̻̫͇̒̕͠","n̵͎͚̼̐́̚","ö̵̦͖͉́̈́͘","p̵̟̟̠̈́̐͘","q̴͙͇͕̔͘͝","r̵̠͙̟̒̿","s̸̪̻̟͐̒̈́","t̵̘͔̞͛̔","ǘ̸̺̫̞̐͠","v̴͙͍͓̓͝","w̸͓͍͍͛́͘","x̸̡̦̘͛͝͠","y̸͔͎͖̓͋̈́","z̴͕͉͑̒̕͜"]
        cursed_txt = ""

        for idx, char in enumerate(txt):
            if char in normal:
                cursed_txt += cursed[normal.index(char)]
            else:
                cursed_txt += char

        await msg.edit(content=cursed_txt)

    @vbot.command(
        name="translate",
        description="Translates your message to another language"
    )
    async def translate(self, ctx, lang, *, txt):
        msg = ctx.message
        await msg.delete()

        try:
            translated = GoogleTranslator(source='auto', target=lang).translate(txt)
        except:
            translated = txt

        await ctx.send(content=translated)

    @vbot.command(
        name="morsecode",
        description="Translates your message to morse code"
    )
    async def morsecode(self, ctx, *, txt):
        msg = ctx.message
        morse = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
            "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
            "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
            "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
            "9": "----.", "0": "-----", ",": "--..--", ".": ".-.-.-", "?": "..--..", "/": "-..-.", "-": "-....-",
            "(": "-.--.", ")": "-.--.-", " ": "/"
        }
        morse_txt = ""

        for char in txt:
            if char.upper() in morse:
                morse_txt += morse[char.upper()] + " "

        await msg.edit(content=morse_txt)

    @vbot.command(
            name="editglitch",
            description="replaces (edited) with an actual (edited) character from discord"
    )
    async def editglitch(self, ctx: vbot.Context, *, text: str):
        msg = ctx.message

        await msg.edit(text.replace("(edited)", "‫"))

    @vbot.command(
        name="regional",
        description="Sends a message in regional indicators"
    )
    async def regional(self, ctx: vbot.Context, *, message: str):
        msg = ctx.message
        await msg.delete()
        letters = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        numbersLetter = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

        final = ""

        message = message.lower()
        for char in message:
            if char in letters:
                final += f":regional_indicator_{char}:"
            elif char in numbers:
                final += f":{numbersLetter[int(char)]}:"
            else:
                if char == "!":
                    final += "❗"
                elif char == "?":
                    final += "❓"
                else:
                    final += char

        await ctx.send(final)

    @vbot.command(
        name="emojisep",
        description="Sends a message with an emoji instead of spaces"
    )
    async def emojisep(self, ctx: vbot.Context, emoji: str, *, message: str):
        msg = ctx.message
        await msg.delete()

        final = ""
        for char in message:
            if char == " ":
                final += f"{emoji}"
            else:
                final += char

        await ctx.send(final)

    @vbot.command(
    name="emojireact",
    description="Reacts to a message with regional indicators and other emojis"
    )
    async def emojireact(self, ctx: vbot.Context, messagelink: str, *, text: str):

        msg = ctx.message
        await msg.delete()

        link = messagelink.split("/")
        channel = self.bot.get_channel(int(link[5]))
        message = await channel.fetch_message(int(link[6]))

        for char in text:
            letters = "abcdefghijklmnopqrstuvwxyz"
            indicators = ["🇦", "🇧", "🇨", "🇩", "🇪", "🇫", "🇬", "🇭", "🇮", "🇯", "🇰", "🇱",  "🇲", "🇳", "🇴", "🇵", "🇶", "🇷", "🇸", "🇹", "🇺", "🇻", "🇼", "🇽", "🇾", "🇿"]
            numbers = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]

            if char.lower() in letters:
                await message.add_reaction(indicators[letters.index(char.lower())])
            if (isinstance(char, int) or char.isdigit()) and int(char) < 10:
                await message.add_reaction(numbers[int(char)])

if __name__ == "__main__":
    print("You need to run main.py to run the bot")


async def setup(bot):
    await bot.add_cog(TextCmds(bot))
