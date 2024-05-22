from pvrecorder import PvRecorder
import wave
import struct


def record():
    recorder = PvRecorder(device_index=0, frame_length=512)
    audio = []
    path = 'audio.mp3'

    recorder.start()
    counter = 0

    while counter <= 120:
        counter += 1
        frame = recorder.read()
        audio.extend(frame)

    recorder.stop()
    with wave.open(path, 'w') as f:
        f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
        f.writeframes(struct.pack("h" * len(audio), *audio))
    recorder.delete()
