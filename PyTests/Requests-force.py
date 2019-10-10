import requests

site = str(input("site: "))

request = requests.get("http://"+ site)
request.encoding

if(request.status_code == 200):
    print("200 OK")
elif(request.status_code == 401):
    print("401 Unauthorized")
elif(request.status_code == 403):
    print("403 Forbidden")
elif(request.status_code == 406):
    print("406 Not Acceptable")

reqhead = request.headers
print(reqhead["Set-Cookie"])

#print(reqhead["Server"], reqhead["Connection"])
