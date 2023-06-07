import os
import time

from extended import gen_sec_pass, change_account_password

from terminalcolorpy import colored

os.system("")
input(
    rf"""
In the file {colored("accounts.txt", "blue")} enter all your accounts in the following format,

name:password

for example,

myRiotName:verysecurepassword454!!
ValorantEnjoyer:kkkkk33!!

You can also specify a second ":" which indicates your desired password. This means that the program will not generate
a random password but rather, it'll use the one you give it. For example,

myRiotName:verysecurepass:thisismynewpassword!!

A new file {colored("new_accounts.txt", "blue")} will be created & updated as the program goes. Click ENTER to start the program.
"""
)
os.system("cls")

with open("accounts.txt", "r+") as file:
    data = file.read().splitlines()
    data = [i.split(":") for i in data]

    for creds in data:
        try:
            username, password = creds
            new_password = gen_sec_pass()
        except ValueError:
            try:
                username, password, new_password = creds
            except ValueError:
                print(
                    colored("[ERROR]", "red"),
                    "Fault account data for this account in accounts.txt! Skipping...",
                )
                continue

        try:
            change_account_password(username, password, new_password, sleep_time=2)
        except ValueError:
            print(
                colored("[ERROR]", "red"),
                "Faulty login data! Skipping...",
            )
            continue

        with open("new_accounts.txt", "a+") as fl:
            fl.write(f"{username}:{new_password}\n")

        if creds == data[-1]:
            break

        print(colored("[INFO]", "#808080"), "10 second delay, soon starting again\n")
        time.sleep(10)

print()
print(
    colored("[INFO]", "#808080"),
    "Program finished. See the new account data in new_accounts.txt",
)
os.system("pause")
