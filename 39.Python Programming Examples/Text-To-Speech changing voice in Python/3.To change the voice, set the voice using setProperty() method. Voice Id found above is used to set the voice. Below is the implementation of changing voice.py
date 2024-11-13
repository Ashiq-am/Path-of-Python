voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

# Use female voice
converter.setProperty('voice', voice_id)

converter.runAndWait()
