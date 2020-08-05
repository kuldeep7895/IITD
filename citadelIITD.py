import urllib.request,urllib.error,urllib.parse
import json
import time
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('paramiko')
ssh = urllib.request.urlopen("https://gist.githubusercontent.com/dufferzafar/8068684e2914bb08ed9d10f3764aacce/raw/f0f651c00096199a278b001323103d42cd7f1b5f/IIT%2520D%2520-%2520Citadel.json")
json = json.loads(ssh.read())
timeline = [json]
tags = list(json.keys())
import paramiko
from scp import SCPClient
host = "col100.iitd.ac.in"
port = 22
username = input("TELL YOUR IITD USERNAME(eg cs1190000): ")
password = input("Enter your kerberos password(Don't worry it's safe): ")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)


print("\n")

print("JUST DOME INFO:")
print("CAN GO BACK USING COMMAND ---->  BACK")
print("JUST ONE DAY OLD PROGRAM SO FULL OF BUGS")
print("FAIR USE IS MUCH APPRECIATED")
print("IT IS OPEN SOURCE MAKE AS MANY CHANGES YOU LIKE")
print("TO SELECT A FILE OR FOLDER JUST TYPE THE NUMBER CORRESPONDING TO IT")
print("FOR E.G. 5. MTL101 THAN YOU SHOULD COMMAND 5 TO OPEN IT ")
print("CONTACT ME AT kuldeepsan09@gmail.com")
print("FILES WILL BE DOWNLOADED IN THE SAME FOLDER YOU RUN YOUR PROGRAM")

def printTotals(transferred, toBeTransferred):
    print("Transferred: {0}\tOut of: {1}".format(transferred, toBeTransferred))


input("READ INSTRUCTIONS: YES OR NO: ")
print("Ï DON'T CARE YES OR NO IT WAS JUST FOR A GAP")
print("Select your option number")



i = 0
while(i<len(tags)):

    print(str(i+1)+" "+tags[i])
    i+=1
index = int(input("TELL YOUR OPTION NUMBER: "))-1
while(True):
    json = json[tags[index]]
    timeline = timeline + [json]
    if(type(json) == str):
        print("DOWNLOADING WAIT A FEW SECONDS ")
        stdin, stdout, stderr = ssh.exec_command("wget https://study.devclub.in"+json.replace(" ","%20"))
        exit_status = stdout.channel.recv_exit_status()          # Blocking call
        if exit_status == 0:

            sftp = ssh.open_sftp()

            file = open(tags[index],'w+')
            i = 0
            while(i<len(tags)):
                print(str(i+1)+" "+tags[i])
                i+=1
            sftp.get(tags[index],tags[index],callback=printTotals)
            stdin, stdout, stderr = ssh.exec_command("rm "+tags[index])
            
            print ("Hurrah File Downloaded")

            file.close()

        else:
            print("SORRY THERE WAS AN ERROR TRY AGAIN", exit_status)
        timeline.pop()
        json = timeline[-1]
        tags = list(json.keys())
    tags = list(json.keys())
    i = 0
    while(i<len(tags)):
        print(str(i+1)+" "+tags[i])
        i+=1

    

    response = input("TELL YOUR OPTION NUMBER: ")
    

    while(response=="BACK"):
        timeline.pop()
        json = timeline[-1]
        tags = list(json.keys())
        i = 0
        while(i<len(tags)):
            print(str(i+1)+" "+tags[i])
            i+=1
        response = input("TELL YOUR OPTION NUMBER: ")

    index = int(response)-1


print("Done")


