cd /Users/AlexG/Documents/GitHub/anki_html
git add .
d=`date +%Y%m%d\(%H:%M:%S\)`
echo $d
git ci -m "update cards.html on date $d"
git push
