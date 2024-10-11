import csv
import subprocess
import os
import random
import string
import re
import secrets
import json


#Twingate-CLI

logintenat = os.environ["TG_TENANT"]
loginapi = os.environ["TG_API"]


loginoutput = subprocess.check_output('python3 ./tgcli.py auth login -t ' + logintenat + ' -a ' + loginapi, shell=True)
session = loginoutput.decode("utf-8").split(":")[1].strip()
print(session)

animals = ['RedFly', 'RedYak', 'GreenFly', 'PinkCat', 'BlueApe', 'GreenYak', 'BlueFly', 'BlackEel', 'RedBoa', 'BlackBat', 'BlackBoa', 'OrangeFox', 'OrangeApe', 'GreenApe', 'WhiteApe', 'PurpleElk', 'RedCow', 'GreenFox', 'YellowFox', 'PinkBoa', 'YellowElk', 'PinkFox', 'GreenBoa', 'RedBat', 'PurpleApe', 'OrangeBat', 'YellowEel', 'OrangeYak', 'RedDog', 'PinkEel', 'PurpleBat', 'OrangeElk', 'BlueBoa', 'OrangeEel', 'GreenCat', 'WhiteDog', 'OrangeCat', 'BlueCat', 'YellowCat', 'GreenCow', 'BlackYak', 'RedCat', 'WhiteFox']

# Print the list
for animal in animals:
   subprocess.call(["python3", "./tgcli.py", "auth", "logout", "-s", animal])



command3 = ["python3", "./tgcli.py", "auth", "logout", "-s", session]
subprocess.call(command3)
