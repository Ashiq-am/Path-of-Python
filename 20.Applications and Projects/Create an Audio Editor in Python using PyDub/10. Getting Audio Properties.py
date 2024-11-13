from pydub.utils import mediainfo

# Get audio properties
audio_info = mediainfo("audio_file.mp3")

# Print audio properties
print("Duration:", audio_info["duration"], "seconds")
print("Sample Rate:", audio_info["sample_rate"], "Hz")
print("Channels:", audio_info["channels"])
