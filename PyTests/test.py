import requests, sys

if len (sys.argv) >= 3:
    host = sys.argv[1]
    port = sys.argv[2]
    url = "http://" + host +":"+ port
    while True:
        r = requests.get(url)
        print(r)
else:
    print ("fail, try again!")