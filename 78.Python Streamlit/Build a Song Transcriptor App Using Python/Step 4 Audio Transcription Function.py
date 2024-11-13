def transcribe_audio(mp3_filepath):
    # Transcribe using whisper
    result = model.transcribe(mp3_filepath)
    transcription = result['text']
    return transcription
