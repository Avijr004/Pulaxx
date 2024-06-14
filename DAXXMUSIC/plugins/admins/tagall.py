from DAXXMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ "** 𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 🤗** ", 
           " **𝒏𝒆𝒆𝒊𝒖𝒎 𝒏𝒂𝒏𝒖𝒎 𝒔𝒆𝒓𝒏𝒕𝒉𝒂𝒆 𝒑𝒐𝒈𝒖𝒎 𝒏𝒆𝒓𝒂𝒎𝒂𝒆** ", 
           " **𝒓𝒐𝒂𝒅 𝒍𝒂 𝒊𝒓𝒖𝒌𝒖 𝒑𝒂𝒍𝒍𝒂𝒎 𝒏𝒆𝒆𝒕𝒉𝒂 𝒆𝒏 𝒄𝒉𝒆𝒍𝒍𝒂𝒎** ", 
           " **𝒂𝒊𝒊 𝒏𝒆𝒆 𝒆𝒏 𝒊𝒅𝒖𝒑𝒂 𝒑𝒂𝒕𝒉𝒂 𝒏𝒂 𝒂𝒕𝒉𝒂 𝒑𝒂𝒕𝒉𝒂** ", 
           " **𝒏𝒂 𝒑𝒐𝒕𝒉𝒖𝒗𝒂 𝒌𝒐𝒗𝒂 𝒑𝒂𝒅𝒂 𝒎𝒂𝒕𝒂 𝒆𝒏𝒂 𝒌𝒐𝒗𝒂 𝒑𝒂𝒅𝒂 𝒗𝒂𝒄𝒉𝒊𝒓𝒂𝒕𝒉𝒂** ", 
           " **𝒏𝒆 𝒆𝒏 𝒊𝒗𝒍𝒐 𝒈𝒖𝒏𝒅𝒂𝒂𝒂𝒂𝒂 𝒊𝒓𝒖𝒌𝒂** ", 
           " **𝒏𝒆 𝒍𝒐𝒐𝒔𝒂 𝒊𝒍𝒂 𝒍𝒐𝒐𝒔𝒖 𝒎𝒂𝒕𝒉𝒊𝒓𝒊 𝒏𝒂𝒅𝒊𝒌𝒖𝒓𝒊𝒚𝒂** ", 
           " **𝒑𝒍𝒔 𝒄𝒂𝒍𝒍 𝒕𝒉𝒆 𝒂𝒎𝒃𝒖𝒍𝒂𝒏𝒄𝒆 𝒖𝒏𝒈𝒂 𝒌𝒂𝒏𝒏𝒖 𝒆𝒏𝒂 𝒔𝒉𝒐𝒐𝒕 𝒑𝒂𝒏𝒊𝒅𝒊𝒄𝒉𝒖** ", 
           " **𝒄𝒂𝒏𝒕𝒆𝒆𝒏 𝒍𝒂 𝒊𝒓𝒖𝒌𝒖 𝒑𝒖𝒇𝒔 𝒖𝒉 𝒖𝒏𝒂𝒌𝒖 𝒆𝒏𝒂𝒌𝒖 𝒍𝒖𝒗𝒔 𝒖𝒉** ", 
           " **𝒏𝒂𝒍𝒍𝒂 𝒔𝒉𝒂𝒗𝒊𝒏𝒈 𝒑𝒂𝒏𝒂 𝒎𝒂𝒍𝒂 𝒌𝒐𝒓𝒂𝒏𝒈𝒖 𝒎𝒂𝒕𝒉𝒊𝒓𝒊 𝒐𝒓𝒖 𝒎𝒖𝒏𝒋𝒊** ", 
           " **𝒖𝒕𝒉𝒖 𝒑𝒂𝒌𝒂𝒕𝒉𝒂 𝒎𝒂𝒎𝒂 𝒗𝒆𝒌𝒂𝒎𝒂 𝒊𝒓𝒖𝒌𝒖** ", 
           " **𝒖𝒏𝒂 𝒑𝒆𝒕𝒉𝒂𝒏𝒈𝒂𝒍𝒂 𝒊𝒍𝒂 𝒔𝒆𝒏𝒋𝒂𝒏𝒈𝒂𝒍𝒂** ", 
           " **𝒏𝒆 𝒆𝒏𝒂 𝒎𝒖𝒍𝒍𝒂 𝒖𝒏𝒂 𝒕𝒉𝒐𝒕𝒂𝒍𝒂𝒆 𝒌𝒖𝒕𝒉𝒖𝒕𝒉𝒖** ", 
           " **𝒕𝒉𝒂𝒎𝒃𝒊 𝒕𝒆𝒂 𝒊𝒏𝒖 𝒗𝒂𝒓𝒂𝒍𝒂** ", 
           " **𝒏𝒂𝒍𝒍𝒂 𝒔𝒂𝒑𝒕𝒖 𝒔𝒂𝒑𝒕𝒖 𝒕𝒉𝒂𝒅𝒊 𝒎𝒂𝒂𝒅𝒖 𝑴𝒂𝒕𝒉𝒊𝒓𝒊 𝒊𝒓𝒖𝒌𝒂** ", 
           " **𝒊 𝒕𝒉𝒊𝒏𝒌 𝑰'𝒎 𝒇𝒂𝒍𝒍 𝒊𝒏 𝒍𝒐𝒗𝒆 𝒘𝒊𝒕𝒉 𝒚𝒐𝒖** ", 
           " **𝒏𝒊𝒈𝒉𝒕 𝒍𝒂𝒎 𝒕𝒉𝒖𝒌𝒂𝒎𝒂𝒆 𝒗𝒂𝒓𝒂𝒍𝒂 𝒏𝒆𝒆𝒕𝒉𝒂 𝒗𝒂𝒓𝒂** ", 
           " **𝒌𝒐𝒍𝒂𝒏𝒕𝒉𝒂 𝒑𝒐𝒊 𝒑𝒂𝒂𝒍 𝒌𝒖𝒅𝒊𝒄𝒉𝒊𝒕𝒖 𝒕𝒉𝒖𝒏𝒈𝒖 𝒑𝒐** ", 
           " **𝒆𝒑𝒂 𝒑𝒂𝒕𝒉𝒂𝒍𝒖 𝒖𝒓𝒖𝒕𝒊𝒕𝒆 𝒊𝒓𝒖 𝑽𝒆𝒓𝒂 𝒗𝒆𝒍𝒂 𝒊𝒍𝒂 𝒍𝒂** ", 
           " **𝒏𝒂 𝒖𝒏𝒂𝒌𝒖 𝒇𝒓𝒏𝒅 𝒂𝒉 𝒌𝒆𝒅𝒂𝒊𝒌𝒂 𝒏𝒆 𝒌𝒖𝒅𝒖𝒕𝒉𝒖 𝒗𝒂𝒄𝒉𝒊𝒓𝒖𝒌𝒂𝒏𝒖** ", 
           " **𝒏𝒆 𝒆𝒏𝒂 𝒑𝒖𝒍𝒊𝒚𝒂** ", 
           " **𝒆𝒏𝒌𝒖𝒅𝒂 𝒑𝒆𝒔𝒂 𝒎𝒂𝒕𝒊𝒚𝒂** ", 
           " **𝒆𝒏 𝒆𝒆𝒆 𝒏𝒖 𝒑𝒂𝒍𝒍𝒂 𝒌𝒂𝒕𝒖𝒓𝒂** ", 
           " **𝒖𝒏𝒌𝒖𝒅𝒂 𝒏𝒂𝒂 𝒅𝒐𝒐𝒐𝒐** ", 
           " **𝒆𝒏𝒌𝒖𝒅𝒂 𝒑𝒆𝒔𝒂 𝒎𝒂𝒕𝒊𝒚𝒂** ", 
           " **𝒏𝒆 𝒓𝒐𝒎𝒃𝒂 𝒄𝒖𝒕𝒆 𝒂𝒉 𝒊𝒓𝒖𝒌𝒂** ", 
           " **𝒔𝒖𝒎𝒂𝒗𝒆 𝒊𝒓𝒖𝒌𝒂 𝒎𝒂𝒕𝒊𝒚𝒂** ", 
           " **𝒂𝒂𝒎𝒂 𝒚𝒂𝒓 𝒏𝒆** ", 
           " **𝒆𝒏𝒂𝒌𝒖 𝒑𝒂𝒔𝒊𝒌𝒖𝒕𝒉𝒖** ", 
           " **𝒏𝒂 𝒖𝒏𝒂𝒌𝒖 𝒐𝒓𝒖 𝒑𝒂𝒂𝒕𝒖 𝒑𝒂𝒅𝒂𝒗𝒂** ", 
           " **𝒖𝒏𝒌𝒊𝒕𝒂 𝒐𝒏𝒖 𝒔𝒐𝒍𝒂𝒏𝒖** ", 
           " **𝒏𝒂 𝒖𝒏𝒂𝒌𝒖 𝒚𝒂𝒓𝒖** ", 
           " **𝒖𝒏𝒂 𝒍𝒂 𝒕𝒉𝒊𝒓𝒖𝒕𝒉𝒂𝒗𝒆 𝒎𝒖𝒅𝒊𝒚𝒂𝒕𝒉𝒖** ", 
           " **𝒏𝒆 𝒍𝒂 𝒉𝒖𝒎𝒂𝒏 𝒕𝒉𝒂𝒏𝒂 𝒅𝒐𝒖𝒃𝒕 𝒂𝒉 𝒊𝒓𝒖𝒌𝒖** ", 
           " **𝒆𝒏 𝒎𝒆𝒍𝒂 𝒑𝒂𝒔𝒂𝒎𝒆 𝒊𝒍𝒂 𝒖𝒏𝒂𝒌𝒖** ", 
           " **𝒏𝒆 𝒖𝒓𝒖𝒕𝒖 𝒖𝒏 𝒏𝒂𝒍𝒍𝒂 𝒎𝒂𝒏𝒂𝒔𝒖𝒌𝒖 𝒏𝒆𝒆𝒕𝒉𝒂 𝒋𝒆𝒊𝒑𝒂** ", 
           " **𝒚𝒐𝒖 𝒃𝒖𝒇𝒇𝒂𝒍𝒐** ", 
           " **𝒑𝒂𝒆** ", 
           " **𝒑𝒂𝒏𝒊** ", 
           " **𝒆𝒓𝒖𝒎𝒂 𝒂𝒅𝒊 𝒗𝒆𝒏𝒖𝒎𝒂** ", 
           " **𝒌𝒂𝒍𝒚𝒂𝒏𝒂𝒎 𝒂𝒈𝒊𝒅𝒖𝒄𝒉𝒂** ", 
           " **𝒑𝒐𝒊 𝒔𝒐𝒏𝒂 𝒌𝒐𝒏𝒅𝒓𝒖𝒗𝒂𝒏** ", 
           " **𝒆𝒏𝒂 𝒕𝒉𝒂𝒗𝒂𝒓𝒂 𝒗𝒆𝒓𝒂 𝒆𝒕𝒉𝒂𝒗𝒂𝒕𝒉𝒖 𝒑𝒐𝒏𝒖 𝒌𝒊𝒕𝒂 𝒑𝒆𝒔𝒖𝒗𝒊𝒚𝒂** ", 
           " **𝒏𝒂𝒏𝒆 𝒌𝒐𝒍𝒂𝒏𝒕𝒉𝒂** ", 
           " **𝒏𝒂 𝒑𝒂𝒗𝒐𝒎 𝒕𝒉𝒂𝒏𝒂** ", 
           " **𝒖𝒏𝒂𝒌𝒖 𝒎𝒂𝒏𝒂𝒔𝒂𝒕𝒄𝒉𝒊 𝒊𝒓𝒖𝒌𝒂** ", 
           " **𝒖𝒏 𝒑𝒆𝒓𝒖 𝒆𝒏𝒂** ", 
           " **𝒄𝒉𝒊𝒊 𝒏𝒂𝒖𝒈𝒉𝒕𝒚𝒚𝒚** ", 
           " **𝒂𝒅𝒊𝒏𝒈 𝒌𝒖𝒕𝒕𝒚 𝒚𝒂𝒂𝒏𝒂** ", 
           " **𝒏𝒂𝒍𝒂 𝒈𝒖𝒏𝒅𝒂 𝒕𝒉𝒂𝒅𝒊𝒚𝒂 𝒑𝒐𝒐𝒔𝒏𝒊𝒌𝒂 𝒎𝒂𝒕𝒉𝒊𝒓𝒊 𝒐𝒓𝒖 𝒎𝒖𝒏𝒋𝒊** ", 
           " **𝒕𝒉𝒖𝒌𝒂𝒎 𝒗𝒂𝒓𝒖𝒕𝒉𝒂 𝒂𝒑𝒂 𝒔𝒂𝒗𝒖** ", 
           " **𝒏𝒂 𝒓𝒐𝒎𝒃𝒂 𝒏𝒂𝒍𝒂 𝒑𝒐𝒏𝒖 𝒕𝒉𝒆𝒓𝒊𝒖𝒎𝒂** ", 
           " **𝒆𝒏𝒂 𝒆𝒕𝒉𝒖𝒌𝒖 𝒆𝒍𝒂𝒓𝒖 𝒔𝒂𝒓𝒂𝒉 𝒔𝒂𝒓𝒂𝒉 𝒏𝒖 𝒌𝒖𝒑𝒖𝒅𝒓𝒂𝒏𝒈𝒂 𝒕𝒉𝒆𝒓𝒊𝒖𝒎 𝒂𝒉 𝒂𝒆𝒏𝒂 𝒆𝒏 𝒏𝒂𝒎𝒆 𝒔𝒂𝒓𝒂𝒉** ", 
           " **𝒂𝒎𝒎𝒂 𝒌𝒊𝒕𝒂 𝒔𝒐𝒍𝒊𝒅𝒖𝒗𝒂** ", 
           " **𝒏𝒂 𝒔𝒂𝒑𝒊𝒅𝒂 𝒑𝒐𝒓𝒂 𝒕𝒂𝒕𝒂** ", 
           " **𝒆𝒏 𝒃𝒐𝒚 𝒇𝒓𝒊𝒆𝒏𝒅 𝒓𝒐𝒎𝒃𝒂 𝒈𝒐𝒐𝒅 𝒃𝒐𝒚 𝒆𝒏𝒂 𝒕𝒉𝒂𝒗𝒂𝒓𝒂 𝒆𝒍𝒂 𝒑𝒐𝒏𝒖 𝒌𝒊𝒕𝒂𝒊𝒖𝒎 𝒑𝒆𝒔𝒖𝒗𝒂𝒏** ", 
           " **𝒏𝒆 𝒆𝒏 𝒕𝒉𝒐𝒏𝒂 𝒕𝒉𝒐𝒏𝒂 𝒏𝒖 𝒑𝒆𝒔𝒊𝒕𝒆 𝒊𝒓𝒖𝒌𝒂** ", 
           " **𝒌𝒂𝒊 𝑽𝒂𝒍𝒊𝒌𝒖𝒕𝒉𝒖 𝒌𝒏𝒋𝒎 𝒌𝒖𝒅𝒂 𝒉𝒆𝒍𝒑 𝒑𝒂𝒏𝒂𝒎𝒂 𝒊𝒓𝒖𝒌𝒂** ", 
           " **𝒖𝒏 𝒔𝒂𝒂𝒗𝒖 𝒔𝒂𝒓𝒂𝒉 𝒌𝒂𝒊𝒍𝒂𝒕𝒉𝒂** ", 
           " **𝒔𝒂𝒓𝒂𝒉 𝒐𝒏 𝒔𝒐𝒈𝒂𝒎** ", 
           " **𝒌𝒖𝒕𝒚 𝒌𝒐𝒍𝒂𝒏𝒕𝒉𝒂** ", 
           " **𝒂𝒅𝒊 𝒗𝒆𝒏𝒖𝒎𝒂** ", 
           " **𝒖𝒏 𝒑𝒂𝒓𝒗𝒂𝒊 𝒆𝒏𝒂𝒊 𝒑𝒂𝒕𝒓𝒂 𝒗𝒂𝒊𝒌𝒖𝒓𝒂𝒕𝒉𝒖** ", 
           " **𝒆𝒏 𝒕𝒉𝒂𝒕𝒉𝒂 𝒂𝒑𝒂𝒗𝒆 𝒔𝒐𝒏𝒂𝒓𝒖 𝒏𝒆 𝒓𝒐𝒎𝒃𝒂 𝒂𝒍𝒂𝒈𝒂 𝒊𝒓𝒖𝒌𝒂𝒏𝒖** ", 
           " **𝒖𝒏𝒂𝒌𝒖 𝒑𝒖𝒅𝒊𝒌𝒖𝒎𝒂 𝒆𝒏𝒂𝒌𝒖 𝒑𝒖𝒅𝒊𝒌𝒖𝒎** ", 
           " **𝒗𝒂𝒏𝒂𝒌𝒂𝒎 𝒆𝒑𝒅𝒊 𝒊𝒓𝒖𝒌𝒊𝒏𝒈𝒂 𝒑𝒂𝒕𝒉𝒖 𝒓𝒐𝒎𝒃𝒂 𝒏𝒂𝒍 𝒂𝒄𝒉𝒖** ", 
           " **𝒆𝒏𝒂𝒌𝒖𝒏𝒆 𝒗𝒂𝒓𝒖𝒗𝒊𝒏𝒈𝒂 𝒍𝒂** ", 
           " **𝒐𝒍𝒖𝒏𝒈𝒂 𝒑𝒐𝒊𝒅𝒖 𝒊𝒍𝒂 𝒄𝒂𝒔𝒆 𝒌𝒖𝒅𝒖𝒕𝒉𝒖𝒓𝒖𝒗𝒂** ", 
           " **𝒏𝒂𝒎𝒂 𝒆𝒏 𝒔𝒂𝒑𝒕𝒖 𝒏𝒊𝒈𝒉𝒕 𝒑𝒆𝒔𝒂 𝒌𝒖𝒅𝒂𝒕𝒉𝒖** ", 
           " **𝒑𝒂𝒊𝒏𝒕 𝒂𝒅𝒊𝒌𝒂 𝒕𝒉𝒆𝒗𝒂 𝒃𝒓𝒖𝒔𝒉 𝒖𝒉 𝒂𝒏𝒕𝒉𝒂 𝒑𝒂𝒊𝒏𝒕 𝒆𝒉 𝒏𝒆𝒆𝒕𝒉𝒂 𝒆𝒏 𝒄𝒓𝒖𝒔𝒉 𝒖𝒉** ", 
           " **𝒂𝒂𝒏𝒂𝒍𝒖𝒎 𝒖𝒏𝒂𝒌𝒖 𝒎𝒐𝒖𝒕𝒉 𝒇𝒂𝒕 𝒌𝒏𝒋𝒎 𝒂𝒕𝒉𝒊𝒈𝒂𝒎 𝒕𝒉𝒂** ", 
           " **𝒃𝒍𝒐𝒐𝒅𝒚 𝒇𝒐𝒐𝒍** ", 
           " **𝒖𝒏𝒂 𝒍𝒂 𝒑𝒆𝒕𝒉𝒂𝒏𝒈𝒂𝒍𝒂 𝒊𝒍𝒂 𝒔𝒆𝒏𝒋𝒂𝒏𝒈𝒂𝒍𝒂** ", 
           " **𝒆𝒏𝒂𝒂𝒂𝒂𝒂 𝒖𝒓𝒖𝒕𝒖𝒖𝒖𝒖𝒖𝒖** ", 
           " **𝒈𝒖𝒏𝒅𝒖𝒖𝒖 𝒃𝒂𝒃𝒚𝒚𝒚𝒚 𝒆𝒏𝒂 𝒑𝒂𝒏𝒓𝒊𝒏𝒈𝒂 𝒚𝒂𝒓𝒂 𝒑𝒂𝒌𝒖𝒓𝒊𝒏𝒈𝒂** ", 
           " **𝒗𝒆𝒆𝒕𝒍𝒂 𝒆𝒍𝒂𝒓𝒖𝒎 𝒏𝒂𝒍𝒂𝒎𝒂** ", 
           " **𝒖𝒏𝒂 𝒑𝒂𝒌𝒂𝒏𝒖𝒎𝒆** ", 
           " **𝒐𝒓𝒖 𝒏𝒂𝒍 𝒖𝒏𝒂 𝒑𝒂𝒌𝒂 𝒗𝒂𝒓𝒖𝒗𝒂** ", 
           " **𝒆𝒏𝒂𝒌𝒖 𝒓𝒐𝒎𝒃𝒂 𝒕𝒊𝒓𝒆𝒅 𝒂𝒉 𝒊𝒓𝒖𝒌𝒖** ", 
           " **𝒏𝒂 𝒑𝒐𝒊 𝒕𝒉𝒖𝒏𝒈𝒂𝒕𝒂** ", 
           " **𝒔𝒂𝒓𝒊 𝒏𝒂 𝒂𝒑𝒓𝒎 𝒗𝒂𝒓𝒂 𝒕𝒂𝒕𝒂 𝒎𝒊𝒄𝒉 𝒚𝒆𝒘** "
          ]

@app.on_message(filters.command(["tagall", "tagmember", "utag", "stag", "hftag", "bstag", "eftag", "tag", "etag", "utag", "atag"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 . ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["tagoff", "tagstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦STOP♦")
