#!/usr/bin/env bash

wget -c "https://zeustracker.abuse.ch/blocklist.php?download=ipblocklist" -O csv/zeustracker-abuse-ipblocklist.csv
wget -c "https://zeustracker.abuse.ch/blocklist.php?download=compromised" -O csv/zeustracker-abuse-compromised.csv
wget -c "http://rules.emergingthreats.net/blockrules/compromised-ips.txt" -O csv/emergingthreats-compromised.csv
wget -c "https://panwdbl.appspot.com/lists/mdl.txt" -O csv/appspot-malwaredomainlist.csv
#wget -c "https://www.dan.me.uk/torlist/?exit" -O csv/tor-exit-nodes.csv
#wget -c "https://www.dan.me.uk/torlist/" -O csv/tor-all-nodes.csv
wget -c "http://data.phishtank.com/data/online-valid.csv" -O csv/phishtank.csv
wget -c "http://dns-bh.sagadc.org/dynamic_dns.txt" -O csv/listdynamic-dns-blocklist.csv
wget -c "https://home.nuug.no/~peter/pop3gropers.txt" -O csv/pop3-gropers-ipblocklist.csv
wget -c "https://ransomwaretracker.abuse.ch/feeds/csv/" -O csv/ransomwaretracker-abuse.csv
wget -c "https://feodotracker.abuse.ch/blocklist/?download=ipblocklist" -O csv/feodotracker-abuse-ipblocklist.csv
wget -c "https://hosts-file.net/psh.txt" -O csv/hosts-file-temp.csv
wget -c "https://hosts-file.net/emd.txt" -O csv/hosts-file-emd-temp.csv
wget -c "http://cinsscore.com/list/ci-badguys.txt" -O csv/cinsscore-ci-badguys.csv
wget -c "http://reputation.alienvault.com/reputation.generic" -O csv/alienvault-generic.csv
wget -c "http://osint.bambenekconsulting.com/feeds/dga-feed-high.csv" -O csv/osint-bambenekconsulting-mal-domains.csv
wget -c "https://sslbl.abuse.ch/blacklist/sslipblacklist.csv" -O csv/sslbl-abuse-ipblacklist.csv
wget -c "https://sslbl.abuse.ch/blacklist/dyre_sslipblacklist.csv" -O csv/dyressl-abuse-ipblacklist.csv
wget -c "https://hosts-file.net/grm.txt" -O csv/hphosts-domains-temp.csv
wget -c "https://blocklist.greensnow.co/greensnow.txt" -O csv/greensnow-ipblocklist.csv
wget -c "http://www.cert.at/static/downloads/data/conficker/all_domains.txt" -O csv/conficker-domains.csv
wget -c "https://urlhaus.abuse.ch/downloads/csv/" -O csv/urlhaus-abuse-malwaredomainlist.csv
wget -c "http://api.cybercure.ai/feed/get_ips?type=csv" -O csv/cybercure-ipblocklist-temp.csv
wget -c "http://api.cybercure.ai/feed/get_url?type=csv" -O csv/cybercure-blocked-urls-temp.csv
wget -c "http://api.cybercure.ai/feed/get_hash?type=csv" -O csv/cybercure-hashes-temp.csv
wget -c "http://www.ipspamlist.com/public_feeds.csv" -O csv/ipspamlist.csv

# File Cleanups
tr ',' '\n' < ./csv/cybercure-ipblocklist-temp.csv > ./csv/cybercure-ipblocklist.csv
tr ',' '\n' < ./csv/cybercure-blocked-urls-temp.csv > ./csv/cybercure-blocked-urls.csv
tr ',' '\n' < ./csv/cybercure-hashes-temp.csv > ./csv/cybercure-hashes.csv
sed -i -e '$a\' ./csv/cybercure-ipblocklist.csv
sed -i -e '$a\' ./csv/cybercure-blocked-urls.csv
sed -i -e '$a\' ./csv/cybercure-hashes.csv

rm -rvf ./csv/cybercure-ipblocklist-temp.csv ./csv/cybercure-blocked-urls-temp.csv ./csv/cybercure-hashes-temp.csv

sed '1,7 {s/^/#/}' ./csv/hosts-file-temp.csv > ./csv/hosts-file.csv
sed '1,7 {s/^/#/}' ./csv/hosts-file-emd-temp.csv > ./csv/hosts-file-emd.csv
sed '1,7 {s/^/#/}' ./csv/hphosts-domains-temp.csv > ./csv/hphosts-domains.csv

rm -rvf ./csv/hosts-file-temp* ./csv/hosts-file-emd-temp* ./csv/hphosts-domains-temp*
