import pygame

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    input("Press Enter to stop playback...")
    pygame.mixer.music.stop()

# Example usage
mp3_file = "example.mp3"
play_mp3(mp3_file)