<div align="center">

# riot-password-changer
<i>Automatically change Riot account passwords using Selenium
</i>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<p>outdated video, cannot be bothered to make a new one. functionally the same however</p>

![Alt Text](https://cdn.discordapp.com/attachments/995797406404857977/1083164624704249876/cli-first-gig.gif)
</div>

# Overview

This is an automatic Riot Games account password changer using these technologies,
- undetected-chromedriver
- python3
- selenium

Instructions on how to use the program are displayed after running the `main.py` file. To quote myself here,

> In the file **accounts.txt** enter all your accounts in the following format,
> 
> `name:password`
> 
> for example,
> 
> `myRiotName:verysecurepassword454!!`

> You can also specify a second "`:`" which indicates your desired password. This means that the program will not generate a random password but rather, it'll use the one you give it. For example,
>
> `myRiotName:verysecurepass:thisismynewpassword!!`
>

> A new file **new_accounts.txt** will be created & updated as the program goes. Click ENTER to start the program.
>
> **Please note that the process is fully autonomous for accounts without a verified email, that is ones that do not require 2FA entry.**

So, essentially:

1. Put your accounts seperated with a newline in accounts.txt in the format `name:password`.
2. Ensure you have an internet connection and atleast Python 3.9 installed.
2. Run `RUN_ME.bat` if you're on Windows otherwise install `requirements.txt` yourself via `py -m pip install -U -r requirements.txt`
3. Run the `main.py` script via `py main.py` or `python main.py` for unix systems

⭐ Stars are apprecitiated!

## Contributing

Please look at the issues for any feature requests. 

