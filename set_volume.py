import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes.client import CreateObject

def set_volume(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_level, None)

def gradually_increase_volume(initial_volume, target_volume, duration, increment):
    steps = int(duration / increment)
    step_size = (target_volume - initial_volume) / steps

    current_volume = initial_volume
    for _ in range(steps):
        current_volume += step_size
        set_volume(current_volume)
        time.sleep(increment)

if __name__ == "__main__":
    initial_volume = 0.40  # Initial volume at 40%
    target_volume = 0.80  # Target volume at 80%
    duration = 40  # Duration to reach target volume in seconds
    increment = 1  # Increment every second

    set_volume(initial_volume)
    gradually_increase_volume(initial_volume, target_volume, duration, increment)
