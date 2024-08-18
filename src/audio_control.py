# audio_control.py

import alsaaudio

def set_audio_input_output():
    # 设置音频输入和输出设备
    input_device = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
    output_device = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK)

    input_device.setchannels(1)
    input_device.setrate(44100)
    input_device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    input_device.setperiodsize(160)

    output_device.setchannels(1)
    output_device.setrate(44100)
    output_device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    output_device.setperiodsize(160)
