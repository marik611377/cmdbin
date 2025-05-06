import requests

version = "1.3\n"

url = "https://raw.githubusercontent.com/marik611377/cmdbin/refs/heads/main/version.cmdbin"
r = requests.get(url)

if version != r.text:
    print("Your version of CMDbin is outdated. Please download the latest version.")
    print("https://github.com/marik611377/cmdbin")