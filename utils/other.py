import os
from datetime import datetime
from colorama import Fore as F
from typing import Any
import config


def clear_console() -> None:
    os.system("clear" if os.name != "nt" else "cls")


if config.timestamps:
    def log(text: Any) -> None:
        time = datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        print(f"{F.LIGHTBLACK_EX}[{time}] {text}")
else:
    def log(text: Any) -> None:
        print(f"{text}")

