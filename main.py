import os
import time

from extended import gen_sec_pass, change_account_password

from terminalcolorpy import colored

os.system("")
input(
    rf"""
Program radi i koristi selenium tehnologiju s specijalnim Chrome webdriverom koji je undetected za vrijeme ovog pisanja
{colored("02/01/2023", "blue")}.

U fajlu {colored("accounts.txt", "blue")} unesi sve accounte u formatu:

IME:SIFRA

primjer,

Mojeime:mojasifra!53
Mojeime12:mojasifra!43
Mojeime53:mojasifra!554
Mojeime23:mojasifra!v

Novi fajl {colored("new_accounts.txt", "blue")} ce bit napravljen s novim siframa. Klikni ENTER da program pocne.
"""
)
os.system("cls")

with open("accounts.txt", "r+") as file:
    data = file.read().splitlines()
    data = [i.split(":") for i in data]

    for creds in data:
        try:
            username, password = creds
        except ValueError:
            print(
                colored("[ERROR]", "red"),
                "Pogresno ime ili sifra uneseno u accounts.txt! Preskacem ovaj account",
            )
            continue

        new_password = gen_sec_pass()
        try:
            change_account_password(username, password, new_password, sleep_time=2)
        except ValueError:
            print(
                colored("[ERROR]", "red"),
                "Pogresni podaci za login! Preskacem ovaj account",
            )
            continue

        with open("new_accounts.txt", "a+") as fl:
            fl.write(f"{username}:{new_password}\n")

        if creds == data[-1]:
            break

        print(
            colored("[INFO]", "#808080"), "Delay od 10 sekundi, uskoro krecem ponovo\n"
        )
        time.sleep(10)

print()
print(
    colored("[INFO]", "#808080"), "Program zavrsen. Novi nalogi su u new_accounts.txt"
)
os.system("pause")
