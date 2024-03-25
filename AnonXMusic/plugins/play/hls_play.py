import asyncio
import os

from pyrogram import Client, filters
from pytgcalls import GroupCallFactory
from pytgcalls.exceptions import GroupCallNotFoundError


CHAT_ID = -1002052767861  # Update with your chat ID
PLAY_URL = "https://prod-ent-live-gm.jiocinema.com/hls/live/2100323/hd_akamai_androidmob_avc_hin_ipl_s1_m1250324/master_720p.m3u8"


app = Client("my_bot")


group_call_factory = GroupCallFactory()


@app.on_message(filters.command("play") & filters.chat(CHAT_ID))
async def play(_, message):
    group_call = group_call_factory.get_group_call()
    try:
        await group_call.join(CHAT_ID)
    except GroupCallNotFoundError:
        await message.reply_text("You must first start a voice chat in this group!")
    else:
        await group_call.start_audio(PLAY_URL)
        await message.reply_text("Playing...")


@app.on_message(filters.command("stop") & filters.chat(CHAT_ID))
async def stop(_, message):
    group_call = group_call_factory.get_group_call()
    await group_call.stop_audio()
    await message.reply_text("Stopped!")


async def main():
    await app.start()
    await idle()


if __name__ == "__main__":
    asyncio.run(main())
