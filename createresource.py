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

for i in range(234, 235):
    segmentname = "IBMC-devqe segment-" + str(i)
    networkrange = "192.168." + str(i) + ".0/24"
    print(segmentname)
    print(networkrange)

    command = ["python3", "./tgcli.py", "-s", session, "resource", "create", "-a", networkrange, "-n", segmentname, "-r", "UmVtb3RlTmV0d29yazozNzc0Mg==", "-g", "R3JvdXA6MTA5MDkw"]
    subprocess.call(command)


command3 = ["python3", "./tgcli.py", "auth", "logout", "-s", session]
subprocess.call(command3)

