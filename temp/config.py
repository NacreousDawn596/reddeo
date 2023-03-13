import os, datetime, praw, random, platform

username: str = "USERNAME"

password: str = "PASSWORD"

client_id: str = "CLIENT-ID"

game: str = "NAME"

client_secret: str = "CLIENT-SECRET"

user_agent: str = f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(1, 200)}.0.4103.97 Safari/537.36"

reddit = praw.Reddit(client_id = client_id, client_secret = client_secret, user_agent = user_agent, username = username, password = password)

subred = reddit.subreddit("SUBREDDIT")

new: list = [u for u in subred.hot(limit = 100) if u.url.split(".")[-1] != "gif" and u.url.split(".")[-1] != "png" and u.url.split(".")[-1] != "jpg"]

videos: list = []

sfolder: str = f"{os.getcwd()}/{game}-{datetime.datetime.now().strftime('%H-%M-%S')}"

dfolder: str = f"{sfolder}/downloads"

clear = lambda: os.system("cls" if platform.uname().system == "Windows" else "clear")

for d in [sfolder, dfolder]:
    try: os.mkdir(d)
    except: pass

