import speech_recognition as sr

"""
if __name__ == '__main__':
    for mic_id, mic_name in enumerate(sr.Microphone.list_microphone_names()):
        print(f'{mic_id}: {mic_name}')
"""

import sounddevice as sd

# Get the list of available audio devices
devices = sd.query_devices()

# Print information about each device
for i, device in enumerate(devices):
    print(f"Device {i+1}: {device['name']}")
    print(f"    Input channels: {device['max_input_channels']}")
    print(f"    Output channels: {device['max_output_channels']}")
    print()



