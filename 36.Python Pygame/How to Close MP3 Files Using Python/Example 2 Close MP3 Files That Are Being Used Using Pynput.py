import multiprocessing
from playsound import playsound
from pynput import keyboard

def play_sound(file_path):
    playsound(file_path)

def on_press(key):
    if p.is_alive():
        p.terminate()
        print("Sound stopped.")
        exit(0)

if __name__ == '__main__':
    p = multiprocessing.Process(target=play_sound, args=("example.mp3",))
    p.start()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()