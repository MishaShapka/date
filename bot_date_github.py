import subprocess as cmd
import os
import datetime
dt_now = str(datetime.datetime.now())

with open("date.txt", "a") as myfile:
    myfile.write(dt_now)
    myfile.write("\n")
cmd.run("cd C:/Users/ShapkaMY/Desktop/github/date", check=True, shell=True)
cmd.run('git add .', check=True, shell=True)
cmd.run('git commit -m "message"', check=True, shell=True)
cmd.run("git push origin", check=True, shell=True)
