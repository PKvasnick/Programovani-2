from contextlib import suppress
import os

with suppress(FileNotFoundError):
    os.remove("mujsoubor.txt")