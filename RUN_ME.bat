echo off
cls
echo Skidanje paketa i provjera paketa...
py -m pip install -U -r requirements.txt
echo Pokretanje programa...
cls
py main.py