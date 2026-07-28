"""
Minimum Time to Fill a Tank (Three Taps / Buckets Puzzle)
==========================================================
A puzzle we were given in high school. Three taps (or buckets) can each fill a tank
on their own in a given time: N1, N2 and N3 seconds. If all three run at the same
time, how long does it take to fill the tank?

My approach: each tap fills a fraction x/N of the tank in x seconds, so together they
fill x/N1 + x/N2 + x/N3. I increase the time t in small steps until the total filled
reaches 1 (a full tank), then convert that time into minutes/seconds.

By default N1=300, N2=540, N3=660 (seconds), which gives about 149 seconds (~2min29).

Author: Mohamed Farouk Ben Salem
"""


def count(N1,N2,N3,x):
    n1=x/N1
    n2=x/N2
    n3=x/N3
    total=n1+n2+n3
    return total
def convmin(x):
    min=0
    s=0
    x1=int(x)
    if int(x)!=x:
        x2=x1+1-x
    for i in range(x1):
        s=s+1
        if s==60:
            min+=1
            s=0
    ch=str(min)+"min"+str(s)+"sec"+str(x2*100)+"millsec"
    return ch
def mintime(N1=300,N2=540,N3=660):
    global total
    total=0
    t=0
    while total<1:
        t+=0.00001
        total=count(N1,N2,N3,t)
    return (t)
print(convmin(mintime()))
print(str(mintime())+"sec")
print(str(mintime()/60)+"min")
        
    
