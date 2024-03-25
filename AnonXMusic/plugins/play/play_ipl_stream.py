import asyncio
from pytgcalls import Client

async def start_audio_stream():
    client = Client(
        "25071254",
        "5cb7bac198160c6dcf76f11da7b26a45",
        bot_token="6795891231:AAHKl2O-rS-63pwBLDKnPOQ-ylza_fL4t6Q",
        context="YOUR_BOT_CONTEXT",
    )

    await client.start()

    chat_id = -1002052767861  # Replace with the ID of the chat where you want to play the audio

    stream = await client.get_stream(
        "https://prod-ent-live-gm.jiocinema.com/hls/live/2100323/hd_akamai_androidmob_avc_hin_ipl_s1_m1250324/master_720p.mp3"
    )

    await client.join_group_call(chat_id, stream=stream)

    await asyncio.sleep(1800)  # Sleep for 1800 seconds (30 minutes)

    await client.leave_group_call(chat_id)
    await client.stop()

asyncio.run(start_audio_stream())
