from telethon import TelegramClient, events
from mode.magic import Magic
import time
magic = Magic()
@events.register(events.NewMessage)
async def magicrun(event):
		if '.magic' in event.raw_text:
			time.sleep(0.3)
			for d in magic.magic:
				time.sleep(0.3)
				await event.edit(d)
