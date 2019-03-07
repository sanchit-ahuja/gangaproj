#!/usr/bin/env python

import sys
import re
import subprocess
import pdftotext
name=str(sys.argv[1])
with open (name,'rb') as f:
    f=pdftotext.PDF(f)

cnt=0
for x in f:
    x=x.strip()
    x=x.lower()
    res=re.findall('the',x)
    cnt+=len(res)


print(cnt)