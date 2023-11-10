from telethon import TelegramClient, events, sync 

import asyncio
@events.register(events.NewMessage(pattern=".sexy"))

async def sexy(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 15)

    #input_str = event.pattern_match.group(1)

    #if input_str == "lovestory":

    await event.edit(" sexy animation")

    animation_chars = [

            "one ❤ story️ ",
            "  😐             😕 \n/👕\         <👗\ \n 👖               /|",    
            "  😉          😳 \n/👕\       /👗\ \n  👖            /|",
            "  😚            😒 \n/👕\         <👗> \n  👖             /|",
            "  😍         ☺️ \n/👕\      /👗\ \n  👖          /|",
            "  😍          😍 \n/👕\       /👗\ \n  👖           /|",
            "  😘   😊 \n /👕\/👗\ \n   👖   /|",
            " 😳  😁 \n /|\ /👙\ \n /     / |",    
            "😈    /😰\ \n<|\      👙 \n /🍆    / |",
            "😅 \n/(),✊😮 \n /\         _/\\/|",
            "😎 \n/\\_,__😫 \n  //    //       \\",
            "😖 \n/\\_,💦_😋  \n  //         //        \\",
            "  😭      ☺️ \n  /|\   /(👶)\ \n  /!\   / \ ",
            "Tugadi 😂..."
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 15])