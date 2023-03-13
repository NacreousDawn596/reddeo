import os, datetime, requests
from config import *

if not os.path.exists(sfolder +'/output.mp4') and new:
    for i in new:
        try:
            print(i.title,"\n" ,i.url, "\n")
            reqDWN = requests.get("https://sd.redditsave.com/download.php?permalink=" + requests.get(i.url).content.split(b'canonicalUrl":"')[1].split(b'"')[0].decode("utf-8") + "&video_url=" + i.url + "/DASH_720.mp4?source=fallback&audio_url=" + i.url + "/DASH_audio.mp4?source=fallback")
            videos.append(reqDWN.content)
            with open(dfolder + "/{}.mp4".format(datetime.datetime.now().strftime('%H-%M-%S')), "wb") as f: f.write(reqDWN.content)
        except: print("\nsomething went wrong. URL skipping\n")

for meme in os.listdir(dfolder): 
    clear()
    if os.popen(f"ffprobe {dfolder}/{meme}; echo $?").read() == "1\n": os.remove(f"{dfolder}/{meme}")

with open(f"{sfolder}/{game}-{datetime.datetime.now().strftime('%H-%M-%S')}.txt", "w") as e:
    clear()
    for m in os.listdir(dfolder): e.write("".join(f"file {dfolder}/{m}\n"))

os.system(f"ffmpeg -f concat -safe 0 -i \"{sfolder}/{game}-{datetime.datetime.now().strftime('%H-%M-%S')}.txt\" -vcodec copy -acodec copy -movflags faststart -c copy {sfolder}/output.mp4")

print("done")
