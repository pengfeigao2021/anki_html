#!/bin/bash
# reset to tag and push changes
set -e
set -x

cd "$(dirname "$0")"
# add files
git add .
d=`date +%Y%m%d\(%H:%M:%S\)`
echo $d
git ci -m "update gre-cards.html on date $d"
git push 
