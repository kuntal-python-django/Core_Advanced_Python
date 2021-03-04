import urllib3

http = urllib3.PoolManager()
websitename = input("Enter the Website name : \n")
res = http.request('GET', websitename)

# Show Status
print(res.status)
data = res.data.decode("utf-8")

# Saving Result
f= open("WebsiteData.txt","w+")
f.write(data)
f.close()