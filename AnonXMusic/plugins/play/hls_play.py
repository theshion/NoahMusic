import asyncio
from pytgcalls import PyTgCalls, idle

async def start_video_stream():
    chat_id = -1002052767861
    app = PyTgCalls()
    await app.start()
    await app.join_group_call(
        chat_id,
        MediaStream(
            'https://prod-ent-live-gm.jiocinema.com/hls/live/2100323/hd_akamai_androidmob_avc_hin_ipl_s1_m1250324/master_720p.m3u8'
        )
    )

async def main():
    await start_video_stream()
    await idle()

if __name__ == "__main__":
    asyncio.run(main())
