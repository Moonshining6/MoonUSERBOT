from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️"
pic = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/a32783a91999e9774054a.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "𝐎𝐏 ѕραм - by ⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
**[⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️](https://t.me/synax10)
◈ •━━━━━★✦♡✦★━━━━━• ◈ 
➪ **𝗠คѕƬєя:**[⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️](https://t.me/ASHWANI10)
➪ **𝗣ƴƬнοи ⩔єяនɨ០ɳ:** `{platform.python_version()}`
➪ **⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️ ⩔єяនɨ០ɳ:** `{__version__}`
➪ **𝗣ƴяο ⩔єяនɨ០ɳ:** `{pyro_vr}`
◈ •━━━━━★✦♡✦★━━━━━• ◈
     """

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from SpamX.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser
