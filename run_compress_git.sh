# reset to tag and push changes
set -e
set -x
base_tag="anki_v1.6"
cd "$(dirname "$0")"
# remove unused commits
git reflog expire --expire=now --all
git gc --prune=now --aggressive
# add files
git reset --soft $base_tag
git add .
d=`date +%Y%m%d\(%H:%M:%S\)`
echo $d
git ci -m "clean up git history"
git push -f
