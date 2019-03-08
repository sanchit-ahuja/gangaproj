#!/usr/bin/env python

import sys
import re
import subprocess
import pdftotext
name=str(sys.argv[1])
with open (name,'rb') as pdffile:
    textfile=pdftotext.PDF(pdffile)

cnt=0
for line in textfile:
    pattern=re.compile(r'\bthe\b',re.IGNORECASE)
    res=pattern.findall(line)
    cnt+=len(res)


print(cnt)