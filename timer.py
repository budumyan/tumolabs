import time
import datetime
import re

def countdown(h, m, s):
    totalSecs = h * 3600 + m * 60 + s
    while totalSecs > 0:
        timer = datetime.timedelta(seconds=totalSecs)
        print(timer)
        time.sleep(1)
        totalSecs -= 1
    print("vsyo")


a = str(input("type the time to count down(h:m:s)\n"))

if (len(a)<=8):
    start = str(a).split(":")
    h = int(start[0])
    m = int(start[1])
    s = int(start[2])
    countdown(int(h), int(m), int(s))
elif "h" in a:
    h = str(a).split("h")[0]
    a = str(a).split("h")[1]
    match = re.search(r'\d+', a)
    if match:
        m=""
        for i in range(match.start(), len(a)-1):
            m+=a[i]
        m = m.split("m")[0]
    a = a.split("m")[1]
    match2 = re.search(r'\d+', a)
    if match2:
        s=""
        for i in range(match.start()-1, len(a)):
            s+=a[i]
        s=s.split("s")[0]
    else:
        m = 0
        s = 0
