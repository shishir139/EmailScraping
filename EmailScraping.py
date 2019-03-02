import urllib.request,re
f = urllib.request.urlopen("https://yourwebsite.com")
s = f.read().decode('utf-8')
print(re.findall(r"\+\d{2}\s?0?\d{10}",s))
a = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)

aUnique = set(a)
newList = list(aUnique)
b = '\n'.join(newList)
print(b)