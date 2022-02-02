from pygame import mixer
import pygame._sdl2 as sdl2
from time import sleep

mixer.pre_init(devicename="CABLE Input (VB-Audio Virtual Cable)",
               frequency=48000, size=-16, channels=2)
mixer.init()

mixer.music.load("sounds/test.wav")
mixer.music.play()

sleep(5)
