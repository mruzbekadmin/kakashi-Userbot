from telethon import TelegramClient, events 
import os
from mode import emojify
import time
import asyncio

@events.register(events.NewMessage(pattern=".emoji(?: |$)(.*)"))
async def itachi(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(
            event, "Write in text..."
        )
        return
    result = ""
    for a in args:
        a = a.lower()
        if a in emojify.oofman:
            char = emojify.offman[emojify.oofman.index(a)]
            result += char
        else:
            result += a
    await event.edit(result)