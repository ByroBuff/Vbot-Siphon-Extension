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

def placeholder(text, ctx):
    text = text.replace(r"%time%", str(datetime.datetime.now().strftime("%H:%M:%S")))
    text = text.replace(r"%date%", str(datetime.datetime.now().strftime("%d/%m/%Y")))
    text = text.replace(r"%server%", str(ctx.guild.name))

    return text