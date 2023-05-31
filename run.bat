@echo off

REM Docker run command
start /B cmd /C "docker run --rm --gpus all -p 50021:50021 voicevox/voicevox_engine:nvidia-ubuntu20.04-latest"

timeout /t 5 /nobreak >nul

REM Run Python script
start /WAIT python main.py

timeout /t 5 /nobreak >nul

REM Close the first Command Prompt window
taskkill /F /FI "WINDOWTITLE eq Administrator: Command Prompt"

timeout /t 2 /nobreak >nul
