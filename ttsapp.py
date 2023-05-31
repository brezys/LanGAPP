import wave
import pyaudio
import keyboard
from datetime import datetime
import sys
import whisper
from dotenv import load_dotenv
import os
import requests
import json
from pathlib import Path
import deepl
from voicevox import Client
import asyncio
from gtts import gTTS
import urllib.parse
from pydub import AudioSegment
from pydub.playback import play
import sounddevice as sd
import soundfile as sf
from elevenlabs import set_api_key, generate, play
import numba
import subprocess
import time
import docker



load_dotenv('myapi.env')
api_key = os.getenv('DEEPL_API_KEY')
set_api_key(os.getenv('ELEVENLAB_API_KEY'))

speaker_id = os.getenv('SPEAKER_ID')

device_id = os.getenv('AUDIO_DEVICE_ID')


def speak(af):
    af = os.path.join(directory_path,af)
    with open(af, 'r', encoding='utf-8',errors='ignore') as file:
        parsed_text = file.read()
    params_encoded = urllib.parse.urlencode({'text': parsed_text, 'speaker': speaker_id})
    request = requests.post(f'http://127.0.0.1:50021/audio_query?{params_encoded}')
    params_encoded = urllib.parse.urlencode({'speaker': speaker_id, 'enable_interrogative_upspeak': True})
    request = requests.post(f'http://127.0.0.1:50021/synthesis?{params_encoded}',json=request.json())

    with open("translated_speech.wav","wb") as outfile:
        outfile.write(request.content)
    #with open(af, 'r', encoding='utf-8',errors='ignore') as file:
    #    text = file.read()
    #    tts = gTTS(text)
    #   audio_file = 'translated_speech.wav'
    #    tts.save(audio_file)
    print("Audio File Saved As: ")#, audio_file)

def speak_spanish(af):
    af = os.path.join(directory_path,af)
    with open(af, 'r', encoding='utf-8',errors='ignore') as file:
        parsed_text = file.read()
    audio = generate(
        text=parsed_text,
        voice="Arnold",
        model='eleven_multilingual_v1'
    )
    with open("translated_speech.wav","wb") as outfile:
        outfile.write(audio)


def read_json_file(file_name):
    with open(file_name, 'r', encoding='utf-8',errors='ignore') as file:
        data = json.load(file)
    return data

def read_text_file(file_n):
    with open(file_n, 'r', encoding='utf-8',errors='ignore') as file:
        returned_text = file.read()
    return returned_text

def translate_language(text, target_lang):
    deepl_client = deepl.Translator(api_key)
    translation = deepl_client.translate_text(text, target_lang=lang_setting)
    return translation






#Audio file to text file (/json)
def transcribe_audio(fileName):
    fileName = output_filename
    model = whisper.load_model("base")
    result = model.transcribe(fileName)
    print(result["text"])
    #open text file
    text_file = open(os.path.join(directory_path,"results_parsed.txt"), "w")
 
#write string to file
    text_file.write(result["text"])
 
#close file
    text_file.close()


def write_translation_to_file(translation, outputName):
    with open(outputName, 'w', encoding='utf-8') as file:
        file.write(str(translation))


#Recording Speech to Audio File
def record_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    frames = []

    while keyboard.is_pressed('b'):
        data = stream.read(1024)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    soundFile = wave.open(output_filename, "wb")
    soundFile.setnchannels(1)
    soundFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    soundFile.setframerate(44100)
    soundFile.writeframes(b''.join(frames))
    soundFile.close()

    print(f"Recording saved as: {output_filename}")


def exit_program():
    print("Exiting Program")
    
    sys.exit(0)

def delete_files_in_directory(del_name):
    if os.path.exists(del_name):
        os.remove(del_name)


def identifyLang():
    print("Choose target language.")
    global lang_setting
    print("ES, JA \n")
    lang_setting = input().upper()
    time.sleep(1)
    
def start_docker():
    docker_command = [
        'docker',
        'run',
        '--rm',
        '--gpus',
        'all',
        '-p',
        '50021:50021',
        'voicevox/voicevox_engine:nvidia-ubuntu20.04-latest'
    ]

    docker_process = subprocess.Popen(docker_command)
    return docker_process
   
def stop_docker(container_name):
    docker_stop = ['docker', 'stop', container_name]
    subprocess.run(docker_stop)

def main():
    global directory_path
    file_path = os.path.abspath(__file__)
    directory_path = os.path.dirname(file_path)
    #os.path.dirname(file_path)
    global output_filename
    global jsonReaderFile
    docker_process = start_docker()
    i = 4
    while i > 0:
        print("Starting in " + str(i) + " seconds")
        i-=1 
        time.sleep(1)

    while True:
        identifyLang()
        target_lang = lang_setting
        time.sleep(2)
        print(target_lang + " chosen.")
        print("Press 'B' to start recording. Release 'B' to stop recording. Press 'O' to stop recording.")
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_filename = f"recordedAudio_{current_time}.wav"
        translated_text_output_filename = f"translatedText_{current_time}.txt"
        key = keyboard.read_key()
        if key == 'b':
            print("Currently Recording")
            record_audio()
            print("Recording stopped. Transcribing audio.")
            transcribe_audio(output_filename)
            print("Transcribing finished. Recording stopped.")
            result_file = os.path.join(directory_path, "results_parsed.txt")

            with open(result_file, "r") as file:
                text = file.read()
            translation = translate_language(text, target_lang)
            write_translation_to_file(translation, translated_text_output_filename)
            jsonReaderFile = translated_text_output_filename
            
            txt = read_text_file(jsonReaderFile)
            print(txt)
           
            if(target_lang == "JA"):
                speak(jsonReaderFile)
                print('Importing audio file. Reading out loud now.')
                #audio_to_play = AudioSegment.from_wav("translated_speech.wav")
                pathfile = os.path.join(directory_path,"translated_speech.wav")

                data, sr = sf.read(pathfile,dtype='float32')
                sd.play(data, sr, device=int(device_id))
                sd.wait()
            if(target_lang == "ES"):
                speak_spanish(jsonReaderFile)
                pathfile = os.path.join(directory_path,"translated_speech.wav")

                data, sr = sf.read(pathfile,dtype='float32')
                sd.play(data, sr, device=int(device_id))
                sd.wait()

            print("Deleting Files")
            
            delete_files_in_directory(output_filename)
            delete_files_in_directory(translated_text_output_filename)
            
            #play(audio_to_play) 
        elif key == 'o':
            break
    container_name = docker_process.args[2]
    stop_docker(container_name)
    exit_program()    
         
if __name__ == "__main__":
    #asyncio.run(main())
    main()

