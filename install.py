import os

os.system("python -m pip uninstall discord")
os.system("python -m pip uninstall discord.py")
os.system("python -m pip uninstall discord.py-self")

os.system("python -m pip uninstall selfcord.py")
os.system("python -m pip install git+https://github.com/dolfies/discord.py-self@renamed#egg=selfcord.py[voice]")
os.system("python -m pip install -r requirements.txt")

os.system("cls")
print("installation complete")
print("Setup your bot now")


with open("config.py", "w") as config:
    config.write(f"""
class config:
    global token; token = '{input("TOKEN: ")}' # Your token
    global prefix; prefix = [
        's.'
    ] # List of prefixes. Can be one or multiple
    global logging; logging = True # Whether to log stuff like people leaving, joining etc.

    global nitro_sniper; nitro_sniper = True
    global nitro_sniper_url; nitro_sniper_url = '' # Nitro sniper URL

    """)