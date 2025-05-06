import os
from os import getcwd
import requests

url = "https://raw.githubusercontent.com/marik611377/cmdbin/refs/heads/main/version.cmdbin"
r = requests.get(url)

print("Got " + r.text)