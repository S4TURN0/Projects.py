import requests
import time

texto = None

try:
    res = requests.post('https://putsreq.com/er1KEMlaN3xovaQnwPFh')
    texto = res.text
except Exception as e:
    print("Requisição deu erro: ", e)

print(texto)

"""
print (res.url)

res.status_code # returns 200
res.elapsed # returns datetime.timedelta(0, 1, 666890)

res.headers['Content-Type']
print (res.headers)
print("------------------------")
print(res.history)
print(res.url)
print(res.status_code)
print (res.encoding)
print (res.elapsed)"""
# returns 'text/html; charset=utf-8