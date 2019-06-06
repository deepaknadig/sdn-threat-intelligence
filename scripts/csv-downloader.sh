#!/usr/bin/env bash

if [ ! -d /home/$USER/intel/feeds/external ]; then
    printf "Creating the intel directory...\n"
    mkdir -p /home/$USER/intel/feeds/external
fi

INTEL_DIR=/home/$USER/intel/feeds/external

wget -c "https://zeustracker.abuse.ch/blocklist.php?download=ipblocklist" -O $INTEL_DIR/001_zeustracker-abuse-ipblocklist.csv
wget -c "https://zeustracker.abuse.ch/blocklist.php?download=compromised" -O $INTEL_DIR/002_zeustracker-abuse-compromised.csv
wget -c "http://rules.emergingthreats.net/blockrules/compromised-ips.txt" -O $INTEL_DIR/003_emergingthreats-compromised.csv
wget -c "https://panwdbl.appspot.com/lists/mdl.txt" -O $INTEL_DIR/004_appspot-malwaredomainlist.csv
wget -c "http://cybercrime-tracker.net/all.php" -O $INTEL_DIR/005_cybercrime-tracker.csv
wget -c "http://data.phishtank.com/data/online-valid.csv" -O $INTEL_DIR/006_phishtank.csv
wget -c "http://dns-bh.sagadc.org/dynamic_dns.txt" -O $INTEL_DIR/007_listdynamic-dns-blocklist.csv
wget -c "http://labs.snort.org/feeds/ip-filter.blf" -O $INTEL_DIR/008_snort-ip-filter.csv
wget -c "https://raw.githubusercontent.com/pan-unit42/iocs/master/diamondfox/diamondfox_panels.txt" -O $INTEL_DIR/009_pan-unit42-diamondfox-panels.csv
wget -c "https://home.nuug.no/~peter/pop3gropers.txt" -O $INTEL_DIR/pop3-gropers-ipblocklist.csv
wget -c "https://ransomwaretracker.abuse.ch/feeds/csv/" -O $INTEL_DIR/ransomwaretracker-abuse.csv
wget -c "https://feodotracker.abuse.ch/blocklist/?download=ipblocklist" -O $INTEL_DIR/feodotracker-abuse-ipblocklist.csv
wget -c "https://hosts-file.net/psh.txt" -O $INTEL_DIR/hosts-file-temp.csv
wget -c "https://hosts-file.net/emd.txt" -O $INTEL_DIR/hosts-file-emd-temp.csv
wget -c "http://cinsscore.com/list/ci-badguys.txt" -O $INTEL_DIR/cinsscore-ci-badguys.csv
wget -c "http://reputation.alienvault.com/reputation.generic" -O $INTEL_DIR/alienvault-generic.csv
wget -c "http://osint.bambenekconsulting.com/feeds/dga-feed-high.csv" -O $INTEL_DIR/osint-bambenekconsulting-mal-domains.csv
wget -c "https://sslbl.abuse.ch/blacklist/sslipblacklist.csv" -O $INTEL_DIR/sslbl-abuse-ipblacklist.csv
wget -c "https://sslbl.abuse.ch/blacklist/dyre_sslipblacklist.csv" -O $INTEL_DIR/dyressl-abuse-ipblacklist.csv
wget -c "https://hosts-file.net/grm.txt" -O $INTEL_DIR/hphosts-domains-temp.csv
wget -c "https://blocklist.greensnow.co/greensnow.txt" -O $INTEL_DIR/greensnow-ipblocklist.csv
wget -c "http://www.cert.at/static/downloads/data/conficker/all_domains.txt" -O $INTEL_DIR/conficker-domains.csv
wget -c "https://urlhaus.abuse.ch/downloads/csv/" -O $INTEL_DIR/urlhaus-abuse-malwaredomainlist.csv
wget -c "http://api.cybercure.ai/feed/get_ips?type=csv" -O $INTEL_DIR/cybercure-ipblocklist-temp.csv
wget -c "http://api.cybercure.ai/feed/get_url?type=csv" -O $INTEL_DIR/cybercure-blocked-urls-temp.csv
wget -c "http://api.cybercure.ai/feed/get_hash?type=csv" -O $INTEL_DIR/cybercure-hashes-temp.csv
wget -c "http://www.ipspamlist.com/public_feeds.csv" -O $INTEL_DIR/ipspamlist.csv
#wget -c "https://www.dan.me.uk/torlist/?exit" -O $INTEL_DIR/tor-exit-nodes.csv
#wget -c "https://www.dan.me.uk/torlist/" -O $INTEL_DIR/tor-all-nodes.csv

# File Cleanups
tr ',' '\n' < $INTEL_DIR/cybercure-ipblocklist-temp.csv > $INTEL_DIR/cybercure-ipblocklist.csv
tr ',' '\n' < $INTEL_DIR/cybercure-blocked-urls-temp.csv > $INTEL_DIR/cybercure-blocked-urls.csv
tr ',' '\n' < $INTEL_DIR/cybercure-hashes-temp.csv > $INTEL_DIR/cybercure-hashes.csv
sed -i -e '$a\' $INTEL_DIR/004_appspot-malwaredomainlist.csv
sed -i -e '$a\' $INTEL_DIR/cybercure-ipblocklist.csv
sed -i -e '$a\' $INTEL_DIR/cybercure-blocked-urls.csv
sed -i -e '$a\' $INTEL_DIR/cybercure-hashes.csv

rm -rvf $INTEL_DIR/cybercure-ipblocklist-temp.csv $INTEL_DIR/cybercure-blocked-urls-temp.csv $INTEL_DIR/cybercure-hashes-temp.csv

sed '1,7 {s/^/#/}' $INTEL_DIR/hosts-file-temp.csv > $INTEL_DIR/hosts-file.csv
sed '1,7 {s/^/#/}' $INTEL_DIR/hosts-file-emd-temp.csv > $INTEL_DIR/hosts-file-emd.csv
sed '1,7 {s/^/#/}' $INTEL_DIR/hphosts-domains-temp.csv > $INTEL_DIR/hphosts-domains.csv

rm -rvf $INTEL_DIR/hosts-file-temp* $INTEL_DIR/hosts-file-emd-temp* $INTEL_DIR/hphosts-domains-temp*
