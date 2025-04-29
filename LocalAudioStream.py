import pyaudio

# Initialize PyAudio with WASAPI support
pa = pyaudio.PyAudio()

# Find the default loopback device
host_api = pa.get_host_api_info_by_type(pyaudio.paWASAPI)
default_idx = host_api['defaultLoopbackDevice']

stream = pa.open(
    format=pyaudio.paInt16,
    channels=2,
    rate=48000,
    input=True,
    frames_per_buffer=960,
    input_device_index=default_idx
)

def audio_generator():
    try:
        while True:
            data = stream.read(960, exception_on_overflow=False)
            yield data
    except GeneratorExit:
        stream.stop_stream()
        stream.close()
        pa.terminate()


if __name__ == "__main__":
    audio_generator()