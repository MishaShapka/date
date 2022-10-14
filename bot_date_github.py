import subprocess as cmd

with open("README.mb", "a") as myfile:
    myfile.write("appended text")

cmd.run("cd C:/Users/ShapkaMY/Desktop/github/date", check=True, shell=True)
cmd.run('git add .', check=True, shell=True)
cmd.run('git commit -m "message"', check=True, shell=True)
cmd.run("git push origin", check=True, shell=True)