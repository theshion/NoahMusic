import asyncio
from pytgcalls import PyTgCalls, idle

async def start_video_stream():
    chat_id = -1002052767861
    app = PyTgCalls()
    await app.start()
    await app.join_group_call(
        chat_id,
        MediaStream(
            'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4'
        )
    )

async def main():
    await start_video_stream()
    await idle()

if __name__ == "__main__":
    asyncio.run(main())
