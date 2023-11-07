import requests

url = "https://www.wikipedia.org/robots.txt"
resp = requests.get(url)
with open("robots.txt", 'w', encoding="utf-8") as f:
    print(str(resp.text), file=f)
