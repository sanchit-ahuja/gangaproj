#!/usr/bin/env python


f=open('CERN.txt','rb')
cnt=0
for x in f:
    x=x.strip()
    x=x.split(' ')
    for i in x:
        if i=='the':
            cnt+=1

f.close()

text_file = open("Output24.txt", "w")
text_file.write(str(cnt))
text_file.close()
print(cnt)