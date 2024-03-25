from pytgcalls import PyTgCalls, idle
from pytgcalls.types import InputMediaAudio

# Initialize PyTgCalls
app = PyTgCalls()

# Define your chat ID and audio stream URL
chat_id = -1002052767861
audio_stream_url = "https://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"

# Function to start playing audio in a group call
async def start_audio_stream():
    await app.start()
    await app.join_group_call(
        chat_id,
        InputMediaAudio(
            audio_stream_url,
            duration=0,  # Set the duration to 0 for indefinite playback
        ),
    )

# Example usage
await start_audio_stream()

# Keep the program running
idle()
