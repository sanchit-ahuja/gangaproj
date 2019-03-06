#!/usr/bin/env python

import sys
name=str(sys.argv[1])
f=open(name,'rb')
cnt=0
for x in f:
    x=x.strip()
    x=x.split(' ')
    for i in x:
        if i=='the':
            cnt+=1


text_file = open("Output.txt", "w")
text_file.write(str(cnt))
text_file.close()
sys.stdout.write(str(cnt) + '\n')
