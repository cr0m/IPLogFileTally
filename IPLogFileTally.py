#
# IP Address pull out and counter for log files
# Set to_strip_out to and pre or post text to the address
# 
# ./testscript.py filename filter
#

import sys
import re
from collections import Counter

file = str(sys.argv[1])
filter = str(sys.argv[2])

ip_regex = "%s=(?:[0-9]{1,3}\.){3}[0-9]{1,3}" % (filter)
to_strip_out = "['%s= '] ', '" % (filter)

logs = []
templist = []
iplist = []
count = 0

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