import requests, sys

host = input("Host/website: ")
Port = input("Port (80/443): ")
if(Port == "80"):    
    url = "http://{}:{}".format(host,Port)
elif(Port == "443"):
    url = "https://{}:{}".format(host,Port)
else:
    print("Invalid port") 
    sys.exit()
try:
    while True:
        r =requests.get(url)
        print(r)
except Exception as e:
    print ("Can't find the hostname or port specified")