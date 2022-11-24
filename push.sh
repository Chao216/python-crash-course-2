#!/bin/bash
time=`date +%Y/%m/%d@%H:%M:%S`
git add *
git commit -m "auto push $time"
git push origin main
echo "auto pushed $time"

