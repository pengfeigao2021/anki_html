# reset to tag and push changes
base_tag="anki_v1.4"
cd /Users/AlexG/Documents/GitHub/anki_html
# remove unused commits
git reflog expire --expire=now --all
git gc --prune=now --aggressive
# add files
git reset --soft $base_tag
git add .
d=`date +%Y%m%d\(%H:%M:%S\)`
echo $d
git ci -m "update cards.html on date $d"
git push -f
