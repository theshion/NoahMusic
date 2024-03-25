import asyncio
from pyrogram import Client
from ntgcalls import PyTgCalls, idle
from ntgcalls.types import MediaStream

CHAT_ID = -1002052767861  # Update with your chat ID
PLAY_URL = 'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4'

app = Client("my_bot")

async def start_audio_stream():
    group_call = PyTgCalls(app)
    await group_call.start()
    await group_call.join_group_call(
        CHAT_ID,
        MediaStream(
            PLAY_URL,
        )
    )

async def main():
    await start_audio_stream()
    await idle()

if __name__ == "__main__":
    app.start()
    asyncio.run(main())
