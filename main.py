import requests, subprocess, os

# you edit this
whitelist = ["levels/doom", "levels/doom2"]
blacklist = ["/deathmatch/"]

# stolen from Todd Gamblin on StackOverflow lol
def find_nth(string, substring, n):
    start = string.find(substring)
    while start >= 0 and n > 1:
        start = string.find(substring, start+len(substring))
        n -= 1
    return start


def spliturl(url):
    out = {}
    out["name"] = url[url.rfind("/")+1:]
    

def roll():
    while True:
        request = requests.get("https://www.doomworld.com/idgames/?random")
        for i in whitelist:
            for j in blacklist:
                if i in request.url and not j in request.url:
                    return request

req = roll()

name = req.url[req.url.rfind("/")+1:]
if not os.path.isdir(name):
    os.mkdir(name)

desc = requests.get("{}.txt".format(req.url.replace("doomworld.com/", "gamers.org/pub/"))).content
with open(f"{name}/{name}.txt", "wb") as f:
    f.write(desc)

wad = requests.get("{}.zip".format(req.url.replace("doomworld.com/", "gamers.org/pub/"))).content
with open(f"{name}/{name}.zip", "wb") as f:
    f.write(wad)

del desc, wad