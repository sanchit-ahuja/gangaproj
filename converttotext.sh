#!/bin/bash

for((c=0;c<=11;c++))
do
    pdftotext document-page$c.pdf
    echo "done $c times"
done
