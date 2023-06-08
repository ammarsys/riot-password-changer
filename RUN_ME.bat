echo off
cls
echo Skidanje paketa i provjera paketa...
py -m pip install -r requirements.txt -U
echo Pokretanje programa...
cls
py main.py