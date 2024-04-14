import screen_brightness_control as sbc
import time
from random import randint

import webbrowser

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_volume_level(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Set the volume level (0.0 to 1.0)
    volume.SetMasterVolumeLevelScalar(level, None)

def unmute_audio():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Unmute
    volume.SetMute(0, None)

if __name__ == "__main__":
    unmute_audio()
    target_volume = 50 / 100  # Converting to a scalar value (0.0 to 1.0)
    set_volume_level(target_volume)

for i in range(0, 25):
    x = randint(1, 100)
    y = randint(5, 15)
    x = x - y
    sbc.set_brightness(x)
    time.sleep(1)
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
#reset
#sbc.setbrightness(75)