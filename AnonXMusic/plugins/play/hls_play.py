import asyncio
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import MediaStream

async def start_audio_stream():
    chat_id = -1002052767861
    app = PyTgCalls(client)
    await app.start()
    await app.join_group_call(
        chat_id, 
        MediaStream(
            'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4',
        )
    )

async def main():
    await start_audio_stream()
    await idle()

if __name__ == "__main__":
    asyncio.run(main())
