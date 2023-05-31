# LanGAPP - Real-Time Natural Translation Service

LanGAPP is an ongoing open-source personal project aimed at developing an efficient and real-time translation service using Python. By leveraging advanced neural networks, voice-to-text, and text-to-voice techniques, the language barrier between English and Spanish, as well as English and Japanese translations, has been not only squashed, but improved upon due to the familiar sounding cadence and intonation of the voices originating from the neural networks.

## Features:
- Real-time translation: Achieve seamless and instant translation between English and Spanish, English and Japanese.
- Natural and familiar experience: By incorporating the cadence and intonation of fluent voices, the translated output feels more natural and familiar.
- Ongoing expansion: LanGAPP is continuously evolving, with plans to incorporate more languages and build additional bridges.

## Future Plans:
- Language expansion: Adding support for additional languages to further enhance communication across cultures.
- Improved user interface: Enhancing the user interface to provide a more intuitive and user-friendly experience.
- Performance optimizations: Optimizing the performance of the neural networks and backend processes to ensure fast and efficient translations.

Please note that while the project is currently on a temporary break for exploration and further development, LanGAPP holds great promise for revolutionizing communication by breaking down language barriers.

## Contributions and Feedback:
Contributions and feedback are welcomed and encouraged. As I am a "newer" programmer breaking into the technology industry; if you are interested in contributing to the project or have any suggestions, please reach out!

Stay tuned for updates as LanGAPP progresses towards providing a powerful and accessible real-time translation service for users worldwide.

## YouTube Video Demonstration
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/hGzyyvre97w/0.jpg)](https://www.youtube.com/watch?v=hGzyyvre97w)


## Change voices (Japanese Only for now)
- Scroll down on the Voicevox official website until you see the characters: https://voicevox.hiroshiba.jp/
- Listen to a bunch to find a voice you like, then copy their name: 'ずんだもん' for instance
- Navigate to the directory and locate the 'JP_SpeechFiles.json' file
- Inside the file 'crtl+f' and paste for 'ずんだもん', and locate one of their many styles' id values (in this instance I chose the first style corresponding to an 'id' of 3)
![image](https://github.com/brezys/LanGAPP/assets/108705036/360095dd-1267-4b15-9d12-d5e9b0ecd606)
- Once you find an 'id' value navigate to the 'myenv.env' file and change the 'SPEAKER_ID=' to that value (in this instance: 'SPEAKER_ID=3')
- And save the file

## Current Pre-Requisites:
(As this application furthers in development most of these will become either included, or done away with through work arounds)
- Docker Running
- VB-Virtual Audio Cable
- Eleven labs API Key 
- DEEPL API Key 
- (Optional Voicevox installed)

### Docker:
1st - Download Docker: https://www.docker.com/

2nd - Create a container for Voicevox in Docker to get familiar: https://hub.docker.com/r/voicevox/voicevox_engine
![image](https://github.com/brezys/LanGAPP/assets/108705036/74596f79-cd8c-4964-b67d-c5fe82732b80)

### VB-Virtual Audio Cable: 
1st - Download and Install the VB-Virtual Audio Cable: https://vb-audio.com/Cable/

2nd - Run the "findmic.py" script in the terminal and locate: 'CABLE Output (VB-AUDIO POINT)'

![image](https://github.com/brezys/LanGAPP/assets/108705036/7a615c71-908b-4ccf-b05a-874c2aa4fff6)

3rd - Go into the 'myenv.env' file and change the 'AUDIO_DEVICE_ID=' and after the '=' paste your audio device number directly after the '=' *no space* (For instance: AUDIO_DEVICE_ID=92) 

### Elevem labs API Key
1st - Make a free account on Elevenlabs: https://beta.elevenlabs.io/speech-synthesis

2nd - Navigate to your 'Profile Settings' by clicking on your profile picture and then copy your API-Key (highlighted in blue)
![image](https://github.com/brezys/LanGAPP/assets/108705036/dff6ea7c-c3d7-4183-ac06-efca3293173a)

3rd - Go into the 'myenv.env' file and change the 'ELEVENLAB_API_KEY=' and after the '=' paste your API-Key directly after the '=' *with no space*

### DEEPL API Key
1st - Make a free account on DEEPL to gain access to their DEEPL REST API: https://www.deepl.com/en/account/

2nd - Navigate to your 'Authentication Key for DeepL API' and then copy your API-Key
![image](https://github.com/brezys/LanGAPP/assets/108705036/ad7c619b-49ce-4233-9777-45941125d9e5)

3rd - Go into the 'myenv.env' file and change the 'DEEPL_API_KEY=' and after the '=' paste your API-Key directly after the '=' *no space*

### (Optional) Voicevox
1st - Download and Install Voicevox here: https://voicevox.hiroshiba.jp/
