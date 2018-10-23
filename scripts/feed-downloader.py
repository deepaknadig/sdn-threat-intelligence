from urllib.request import urlopen
import re, csv, os, hashlib

urlpath =urlopen('https://www.circl.lu/doc/misp/feed-osint/')
string = urlpath.read().decode('utf-8')

pattern = re.compile('[0-9a-zA-Z\-]*.json') #the pattern actually creates duplicates in the list

filelist2 = pattern.findall(string)
filelist = list(set(filelist2))
# print(filelist)

total = len(filelist)
start = 1

# New line Byte
newlines_str = '\n\n\n'
newlines = newlines_str.encode("utf-8")

for filename in filelist:
    if filename != "manifest.json":
        print("Downloading file {}/{}: {}...".format(start,total,filename))
        remotefile = urlopen('https://www.circl.lu/doc/misp/feed-osint/' + filename)
        localfile = open(filename,'wb')
        localfile.write(remotefile.read())
        localfile.write(newlines)
        localfile.close()
        remotefile.close()
        print("Completed.")
        start += 1
