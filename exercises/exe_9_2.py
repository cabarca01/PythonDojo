import re

# From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008

fhandler = open("../data/mbox-short.txt")
pattern = re.compile("^From .* ([0-9][0-9]):", flags=re.IGNORECASE)
morning = 0
afternoon = 0

for line in fhandler:
    line = line.rstrip()
    if pattern.match(line):
        for hour in pattern.findall(line):
            if int(hour) <= 12:
                morning += 1
            else:
                afternoon += 1

fhandler.close()
print ("Morning emails: %d \nAfternoon Emails: %d" %(morning, afternoon))
