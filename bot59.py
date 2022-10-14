import subprocess as cmd
def git_push_automation():
    try:
        cp = cmd.run("C:/Users/ShapkaMY/Desktop/github/date", check=True, shell=True)
        print("cp", cp)
        cmd.run('git commit -m "message"', check=True, shell=True)
        cmd.run("git push -u origin master -f", check=True, shell=True)
        print("Success")
        return True
    except:
        print("Error git automation")
        return False

git_push_automation()