from configparser import ConfigParser

parser = ConfigParser()
parser.read(".\\config.ini")

# create a Settings class to hold the settings of the application
class Settings:
    def __init__(self):
        self.audio_device = parser.get("settings", "audio_device")
        self.audio_folder = parser.get("settings", "audio_folder")
        self.user_audio_playback = parser.get("settings", "user_audio_playback")
        self.keybinds = parser.items("keybinds")
