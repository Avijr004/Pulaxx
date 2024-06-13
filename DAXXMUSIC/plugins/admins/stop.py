from pyrogram import filters
from pyrogram.types import Message

from DAXXMUSIC import app
from DAXXMUSIC.core.call import DAXX
from DAXXMUSIC.utils.database import set_loop
from DAXXMUSIC.utils.decorators import AdminRightsCheck
from DAXXMUSIC.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    filters.command(["end", "stop", "cend", "cstop"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await DAXX.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    photo_url = "https://te.legra.ph/file/5f3347d579c92e984521f.jpg"  # Replace with the URL of the photo you want to send    
    await message.reply_photo(
        photo=photo_url          
    )
    await message.reply_text(
        _["admin_9"].format(message.from_user.mention), disable_web_page_preview=True
    )
