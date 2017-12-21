import os

os.system('path=%PATH%;"C:\Program Files\Git\cmd"')
os.system("pep8 MyBot.py > pep8_report.txt")

message = input("Enter commit message:")

os.system("git add -A")
os.system("git commit -m \"" + message +"\"")
os.system("git push origin HEAD")

os.system("zip MyBot.zip MyBot.py hlt\*")
os.system("python ..\hlt_client\hlt_client\client.py bot -b MyBot.zip")