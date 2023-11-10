from telethon import TelegramClient, events, sync 
from telethon.errors import rpcbaseerrors
import time
##
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.utils import get_input_location

from datetime import datetime


@events.register(events.NewMessage(outgoing=True, pattern='\.type'))
async def type(event):
	       if ".type" == event.raw_text[:5]:
	       	orig_text = event.raw_text.split(".type ", maxsplit=1)[1]
	       	text = orig_text
	       	pb = "" 
	       	typing_symbol = "•"
	       while(pb != orig_text):
	               try:
	               	await event.edit(pb + typing_symbol)
	               	time.sleep(0.05)
	               	pb += text[0]
	               	text = text[1:]
	               	await event.edit(pb)
	               	time.sleep(0.05)
	               except Exception  as e:
	               	print(e)