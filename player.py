# 3rd party module imports
from pygame import mixer
import pygame._sdl2 as sdl2
from time import sleep

# Local module imports
from config import Settings


class Player:
    # Initialize the player
    def __init__(self):
        # Get the settings from the config file
        self.settings = Settings()

        # Initialize the mixer
        mixer.pre_init(
            devicename=self.settings.audio_device
            #     frequency=self.settings.audio_frequency,
            #     size=self.settings.audio_size,
            #     channels=self.settings.audio_channels
        )
        mixer.init()

    def load_audio_file(self, filename):
        # Load the audio file
        mixer.music.load(filename)

    def play_audio_file(self):
        if not mixer.get_busy():
            mixer.music.play()
