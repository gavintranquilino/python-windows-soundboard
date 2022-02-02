from configparser import ConfigParser

config = ConfigParser()

# General Settings
config["settings"] = {
    "audio_device": "default",
    "audio_folder": "sounds",
    "user_audio_playback": "true",
}

# Keybinds
config["keybindings"] = {"play_pause": "space", "f1": "test.wav", "f2": "test2.wav"}

with open("config.ini", "w") as configfile:
    config.write(configfile)
