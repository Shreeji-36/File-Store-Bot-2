from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup

#===============================================================#

async def texts(client, query):
    msg = f"""<blockquote>**Tᴇxᴛ Cᴏɴғɪɢᴜʀᴀᴛɪᴏɴ:**</blockquote>
**Start Message:**
<pre>{client.messages.get('START', 'Empty')}</pre>
**Force Sub Message:**
<pre>{client.messages.get('FSUB', "<b>◈ Hᴇʏ  {update.effective_user.mention_html()} ×</b>\n
"<blockquote expandable><b>›› Yᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ. Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟs ᴘʀᴏᴠɪᴅᴇᴅ ʙᴇʟᴏᴡ, ᴛʜᴇɴ ᴛʀʏ ᴀɢᴀɪɴ.. !</b></blockquote>\n\n
<b>››❗Fᴀᴄɪɴɢ ᴘʀᴏʙʟᴇᴍs, ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ : <a href='https://t.me/Prince_Vegeta_36'>𝗖𝗵𝗿𝗼𝗹𝗹𝗼</b></a>")}</pre>
**About Message:**
<pre>{client.messages.get('ABOUT', 'Empty')}</pre>
**Reply Message:**
<pre>{client.reply_text}</pre>
    """
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(f'ꜱᴛᴀʀᴛ ᴛᴇxᴛ', 'start_txt'), InlineKeyboardButton(f'ꜰꜱᴜʙ ᴛᴇxᴛ', 'fsub_txt')],
        [InlineKeyboardButton('ʀᴇᴘʟʏ ᴛᴇxᴛ', 'reply_txt'), InlineKeyboardButton('ᴀʙᴏᴜᴛ ᴛᴇxᴛ', 'about_txt')],
        [InlineKeyboardButton('◂ ʙᴀᴄᴋ', 'settings')]]
    )
    await query.message.edit_text(msg, reply_markup=reply_markup)
    return

#===============================================================#

@Client.on_callback_query(filters.regex("^start_txt$"))
async def start_txt(client: Client, query: CallbackQuery):
    await query.answer()
    ask_text = await client.ask(query.from_user.id, "Send new start text message in the next 60 seconds, send `0` to cancel or wait 60 seconds!\n\n__Note you can use both markdown and html formatting!__", filters=filters.text, timeout=60)
    try:
        text = ask_text.text
        if text == '0':
            return await ask_text.reply("__Start text has not changed!__")
        client.messages['START'] = text
        await texts(client, query)
        return await ask_text.reply("__Start text has been changed!__")
    except Exception as e:
        return client.logger(__name__, client.name).error(e)

#===============================================================#

@Client.on_callback_query(filters.regex("^fsub_txt$"))
async def force_txt(client: Client, query: CallbackQuery):
    await query.answer()
    ask_text = await client.ask(query.from_user.id, "Send new force sub text message in the next 60 seconds, send `0` to cancel or wait 60 seconds!\n\n__Note you can use both markdown and html formatting!__", filters=filters.text, timeout=60)
    try:
        text = ask_text.text
        if text == '0':
            return await ask_text.reply("__Force Sub text has not changed!__")
        client.messages['FSUB'] = text
        await texts(client, query)
        return await ask_text.reply("__Force Sub text has been changed!__")
    except Exception as e:
        return client.logger(__name__, client.name).error(e)

#===============================================================#

@Client.on_callback_query(filters.regex("^about_txt$"))
async def about_txt(client: Client, query: CallbackQuery):
    await query.answer()
    ask_text = await client.ask(query.from_user.id, "Send new about text message in the next 60 seconds, send `0` to cancel or wait 60 seconds!\n\n__Note you can use both markdown and html formatting!__", filters=filters.text, timeout=60)
    try:
        text = ask_text.text
        if text == '0':
            return await ask_text.reply("__About text has not changed!__")
        client.messages['ABOUT'] = text
        await texts(client, query)
        return await ask_text.reply("__About text has been changed!__")
    except Exception as e:
        return client.logger(__name__, client.name).error(e)

#===============================================================#

@Client.on_callback_query(filters.regex("^reply_txt$"))
async def reply_txt(client: Client, query: CallbackQuery):
    await query.answer()
    ask_text = await client.ask(query.from_user.id, "Send new reply text message in the next 60 seconds, send `0` to cancel or wait 60 seconds!\n\n__Note you can use both markdown and html formatting!__", filters=filters.text, timeout=60)
    try:
        text = ask_text.text
        if text == '0':
            return await ask_text.reply("__Reply text has not changed!__")
        client.reply_text = text
        await texts(client, query)
        return await ask_text.reply("__Reply text has been changed!__")
    except Exception as e:
        return client.logger(__name__, client.name).error(e)