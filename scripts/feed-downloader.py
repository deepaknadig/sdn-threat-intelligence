from urllib.request import urlopen, Request
import re, csv, os, hashlib

urllist = [ 'https://www.circl.lu/doc/misp/feed-osint/',
            'http://www.botvrij.eu/data/feed-osint/',
            'https://feeds.inthreat.com/osint/misp/'
        ]

target = r"/home/ubuntu/intel/json"
if not os.path.exists(target):
    os.makedirs(target)

for url in urllist:
    print("_____________________________________________________________________\n")
    print("Downloading from the url: {}".format(url))
    print("_____________________________________________________________________\n")
    req = Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0' # (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36
        }
    )

    urlpath =urlopen(req)

    string = urlpath.read().decode('utf-8')
    pattern = re.compile('[0-9a-zA-Z\-]*.json') #the pattern actually creates duplicates in the list

    filelist2 = pattern.findall(string)
    filelist = list(set(filelist2))

    total = len(filelist)
    start = 1

    # New line Byte
    newlines_str = '\n\n\n'
    newlines = newlines_str.encode("utf-8")

    for filename in filelist:
        if filename != "manifest.json":
            print("Downloading file {}/{}: {}...".format(start,total,filename))
            urljson = url + filename
            reqjson = Request(
                urljson,
                data=None,
                headers={
                    'User-Agent': 'Mozilla/5.0' # (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36
                }
            )

            remotefile = urlopen(reqjson)
            full_filename = os.path.join(target, filename)
            with open(full_filename, 'wb') as f:
                f.write(remotefile.read())
                f.write(newlines)
                f.close()
            remotefile.close()
            print("Completed.")
            start += 1
        else:
            start += 1
