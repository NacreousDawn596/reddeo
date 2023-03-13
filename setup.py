import platform, os, shutil

p = os.getcwd()

config = p + (r"\temp\config.py" if platform.uname().system == "Windows" else r"/temp/config.py")

shutil.copy(config, p)

os.remove(config)

os.system("pip install datetime praw requests -U")

os.system("cls" if platform.uname().system == "Windows" else "clear")

print("done\n")

print("edit ./config.py before you execute ./main.py")
