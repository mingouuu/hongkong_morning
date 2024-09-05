import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes.client import CreateObject

def set_volume(volume_level):
    """
    立即设置主音量到指定级别。

    参数:
    - volume_level (float): 音量级别，范围为0到1。
    """
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_level, None)

def gradually_increase_volume(initial_volume, target_volume, duration, increment):
    """
    逐渐增加音量，从初始音量到目标音量，使用指定的持续时间和增量。

    参数:
    - initial_volume (float): 起始音量级别。
    - target_volume (float): 目标音量级别。
    - duration (int): 完成音量变化的总时间（秒）。
    - increment (int): 每次音量变化的时间间隔（秒）。
    """
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