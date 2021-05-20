import urllib3

http = urllib3.PoolManager()
r = http.request('get', "www.google.de")
print(r.status)
print(r.data)
print(type(r.data))
print(r.data[7798])
with open("source_code.txt", "wb") as fid:
    fid.write(r.data)
    fid.close()