def load_whisper_model():
    model = whisper.load_model("base")
    return model


model = load_whisper_model()
