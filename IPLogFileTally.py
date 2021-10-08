#
# IP Log File Tally - Pll out and count from log file 
# Set to_strip_out to and pre or post text to the address
#

import re
from collections import Counter

file = "FILE_NAME.log"

# set up for destination IP syntax (for fortinet)
# change "dstip=" out for whatever
ip_regex = 'dstip=(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
to_strip_out = "['dstip= ']"

logs = []
templist = []
count = 0
iplist = []

with open(file) as log_file:
    for log_entry in log_file:
        logs.append(log_entry)

        ip = re.findall(ip_regex,log_entry)

		# Tally up unique IPs
        for i in ip:
            if i not in templist:
                count = count + 1
                templist.append(i)
        sip = str(ip)
        test = sip.strip(to_strip_out)
        iplist.append(test)


print("Number of unique IPS", count)
collectedIPS = Counter(iplist)
for key,value in sorted(collectedIPS.items()):
    print(key, value)