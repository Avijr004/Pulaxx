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
        ####
        
quotes = [ " **🥰நாம் நேசிப்பவர் நம்மையும் நேசித்தால் அதை விட சந்தோஷம் வேறு எதுவும் இல்லை🥰**",
           " **🤗உயிராக இருப்பவர்களிடம் உரிமையாக இருப்பதை காட்டிலும் உண்மையாக இருப்பது தான் முக்கியம்🤗**",
           " **நீ நிலவும் இல்லை நட்சத்திரமும் இல்லை இவைகளை எல்லாம் அள்ளி சூடிக்கொள்ளும் வானம் நீ...!!!!! ** ",
           " **🙂நீ இல்லாமல் நான் இல்லை என்பது கூட பொய்யாக இருக்கலாம் ஆனால், உன்னை நினைக்காமல் நான் இல்லை என்பதே மெய்!🙂** ",
           " **🤧நீ என்னை விட்டு விலக நினைக்கும் அந்த நொடிக்கு முன் நீ நினைத்து பார்க்க முடியாத தூரத்திற்கு நான் சென்றிருப்பேன்...🤧** ",
           " **😘விட்டு கொடுத்து வாழ்வது மட்டுமல்ல காதல்  கடைசி வரைக்கும் விட்டு விடாமல் வாழ்வதும் தான் காதல்😘** ",
           " **🤔புரிந்துக்கொள்ளும் வரை எதையும் ரசிக்கவில்லை புரிந்துக்கொண்டபின் உன்னை தவிர எதையும் ரசிக்கமுடியவில்லை.🤔** ",
           " **😚Each day with you is a wonderful addition to my life's journey. I can't wait for forever together.😚** ",
           " **☺You are the perfect woman for me—my everything. I love you.☺** ",
           " **😩No other woman in the world can hold a candle to your beauty, charm, and grace.😩** ",
           " **😋Your voice is my favorite sound, and your smile is my favorite sight. I love you so much.😋** ",
           " **😏You make me feel like the most special woman on earth. I am so lucky to love you.😏** ",
           " **😴Every day is a blessing when it ends by your side. Good night, my love.😴** ",
           " **😙If I had a flower for every time I thought of you… I could walk through my garden forever.😙** ",
           " **😎தோள் கொடுக்க தோழனும் தோள் சாய தோழியும் கிடைத்தால் அவர்கள் கூட தாய் தந்தை தான்!😎** ",
           " **🤩ஒரு நல்ல தோழி மட்டும் இருந்தால் போதும் தோல்வியையும் துவட்டி போட்டு விடலாம்🤩**",
           " **😅நட்பு எப்போதுமே வித்தியாசமானது சில நேரங்களில் அழுத நாட்களை சிரிக்க வைக்கும் சில நேரங்களில் சிரித்த நாட்களை நினைத்து அழ வைக்கும்.😅** ",
           " **😮உலகில் உள்ள அனைவரும் உன்னை விட்டு விலகும் போதும், உன்னுடன் இருப்பவனே உண்மையான நண்பன் ..😮** ",
           " **😣கடலில் நின்று கலசத்தை கவிழ்த்தான் சாம்பலாக கரைந்து சென்றார் நீந்த கற்றுக்கொடுத்த தந்தை. கேட்டதில் வலித்தது😣** ",
           " **😥சிரித்த நிமிடங்களை விட, அழுத நிமிடங்களே... என்றும் மனதை விட்டு நீங்குவதில்லை.... ஞாபகங்கள்😥** ",
           " **🙂நம்ம இல்லாம சந்தோஷமா இருப்பாங்கன்னா... விலகியும் போகலாம், விட்டும் போகலாம். தப்பே இல்ல. போகட்டும் விடுங்க.🙂** ",
           " **😔அனைவரும் அருகில் இருந்தும் அனாதைபோல் உணர வைக்கின்றது நாம் நேசித்தவரின் பிரிவு😔** ",
           " **😌நேரமில்லாத நேரத்திலும் உன்னுடன் பேசினேன்! நீ நேரம் போவதற்காக, பேசுகிறாய் என்று கொஞ்சம் கூட தெரியாமல்!😌** ",
           " **😭எண்ணம் போல் வாழ்க்கை அமையவில்லை என்றாலும் என் எண்ணத்தில் என்றும் வண்ணம் நீ தான்.😭** ",
           " **😓பிறப்பில் இருந்து இறப்பு வரை பிரிவில் தான் முடிகிறது காதல் மட்டுமே பிரிந்தும் பிரிய முடியாத வலியாய் தொடர்கிறது.!😓** ",
           " **🤥Never develop any mysticism, about love; for love itself is a mystic thing that puts you in a mystic situation.🤥** ",
           " **😖“I wish I could hurt you the way you hurt me. But I know that If I had the chance, I wouldn’t do it.😖** ",
           " **🤧“The worst kind of hurt is betrayal because it means someone was willing to hurt you just to make themselves feel better.🤧** ",
           " **😩“Your love brought me to the light, and now that you’re gone how am I supposed to see?😩** ",
           " **🙂“It isn’t the bad memories that make you sad, but the best ones that you can’t bring  back.🙂** ",
           " **😣“Nothing hurts more than realizing you meant everything to me, and I meant nothing to you.😣** ",
           " **😢“Everybody knows that something is wrong between us but nobody knows what’s going on.😢** ",
           " **😭“Boys don’t know how to show their love, but their love is true.😭** ",
           " **😣“I would always keep the good memories in which we are together no matter how badly it has ended.😣** ",
           " **☺"A friend is one soul abiding in two bodies.☺** ",
           " **🥰“True friends are those who you can disagree with and still respect.🥰** ",
           " **🤗“Friendship is the inexplicable connection that makes two souls one.🤗** ",
           " **🤍“True friends are those who you can be vulnerable with and still feel safe.🤍** ",
           " **🖤“True friends are those who make your life a little funnier, a little easier, and a whole lot better.🖤** " ]

# Command
    


@app.on_message(filters.command(["quotes"], prefixes=["/", "@", "#"]))
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
        return await message.reply("/quotes  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/quotes  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/quotes  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
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
                txt = f"{usrtxt} {random.choice(quotes)}"
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


#

@app.on_message(filters.command(["qustop", "quotesoff"]))
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
        return await message.reply("♦ OFFFFFFFFF♦")
